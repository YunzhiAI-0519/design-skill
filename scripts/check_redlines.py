#!/usr/bin/env python3
"""
MiniRelax 落地页设计语言（v2）—— 红线自检脚本

扫描产物目录中的 HTML/CSS/JSX/TSX/Vue/Svelte/Astro 文件，检出可确定判定的红线违规。

错误级（必须修复）:
  E1  transition: all                        —— F3
  E2  黑色阴影                                —— F2

警告级（建议修复，含启发式判断）:
  W1  含动效但缺 prefers-reduced-motion 降级
  W2  含 position: fixed 但缺 env(safe-area-inset-*) 安全区处理   —— F7
  W3  出现 emoji（功能图标应改用 SVG 线性图标）
  W4  含 position: fixed 但既无 backdrop-filter 也无 box-shadow（浮起感不足）—— F6
  W5  transition 中包含触发布局的属性（width/height/top/left/margin/padding/font-size 等）—— F3
  W6  使用 content-visibility: auto 但缺 contain-intrinsic-size  —— F8

说明:
  - F1（低对比灰字压灰底）、F5（flex 子项 min-width:0）依赖运行时/语义判断，脚本无法可靠静态检出，
    请在交付自检清单中人工确认。
  - 页脚区域指示符（🇨🇳 / 🇭🇰 等 U+1F1E6–1F1FF）不计为 emoji 图标。

用法:
  python check_redlines.py <dir-or-file> [更多路径...] [--quiet]

退出码: 发现 E 级错误返回 1，否则返回 0。
"""

import argparse
import re
import sys
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".scss", ".jsx", ".tsx", ".js", ".ts",
        ".vue", ".svelte", ".astro"}

TRANSITION_ALL = re.compile(r"transition\s*:\s*all\b", re.I)

# transition(-property) 中包含触发布局的属性
LAYOUT_PROPS = r"(?:width|height|top|right|bottom|left|gap|inset[\w-]*|margin[\w-]*|padding[\w-]*|font-size|border-width|flex[\w-]*|grid[\w-]*)"
LAYOUT_TRANSITION = re.compile(
    rf"transition(?:-property)?\s*:[^;{{}}]*\b{LAYOUT_PROPS}\b", re.I
)

BLACK_SHADOW = re.compile(
    r"box-shadow\s*:[^;{}]*"
    r"(?:rgba\(\s*0\s*,\s*0\s*,\s*0|#000(?:000)?\b|\bblack\b)",
    re.I,
)

FIXED = re.compile(r"position\s*:\s*fixed", re.I)
BACKDROP = re.compile(r"backdrop-filter", re.I)
SHADOW = re.compile(r"box-shadow\s*:", re.I)

MOTION = re.compile(r"(@keyframes|animation\s*:|transition\s*:)", re.I)
REDUCED = re.compile(r"prefers-reduced-motion", re.I)

SAFE_AREA = re.compile(r"env\(\s*safe-area-inset", re.I)

CONTENT_VIS = re.compile(r"content-visibility\s*:\s*auto", re.I)
CONTAIN_SIZE = re.compile(r"contain-intrinsic-size", re.I)

# 常见 emoji 区段（避开 U+1F1E6–1F1FF 区域指示符 = 国旗，页脚地域标识允许）
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F0FF]"
)

SKIP_DIRS = {"node_modules", ".git", ".next", "dist", "build", "out", ".cache"}


def iter_files(paths):
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            yield p
        elif p.is_dir():
            for child in p.rglob("*"):
                if child.is_file() and child.suffix.lower() in EXTS:
                    if not any(part in SKIP_DIRS for part in child.parts):
                        yield child


def read(path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def strip_comments(text):
    """清空注释内容但保留换行，避免注释里出现 'transition:all' 等关键词造成误报。"""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"/\*.*?\*/", blank, text, flags=re.S)
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    return text


def find_issues(raw_text, project_has_reduced=False):
    """返回 issue 列表: (line_no, code, message, snippet)；line_no=0 表示文件级。

    project_has_reduced: 本次扫描集合中是否存在 prefers-reduced-motion 降级块。
    多文件项目常把降级块集中放在一个 CSS 文件里，按文件判断会误报，故下沉为项目级判断。
    """
    issues = []
    text = strip_comments(raw_text)

    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("//"):     # JS 行注释
            continue
        if TRANSITION_ALL.search(line):
            issues.append((i, "E1",
                           "使用了 transition: all —— 只允许过渡 opacity / transform / border-color / color",
                           line.strip()[:120]))

        if LAYOUT_TRANSITION.search(line):
            issues.append((i, "W5",
                           "transition 中包含触发布局的属性 —— 应改用 transform / opacity",
                           line.strip()[:120]))

        if BLACK_SHADOW.search(line):
            issues.append((i, "E2",
                           "检测到黑色阴影 —— 阴影必须是蓝主色系「大距离 + 低透明度」",
                           line.strip()[:120]))

        if EMOJI.search(line):
            issues.append((i, "W3",
                           "检测到 emoji —— 功能图标应改用 SVG 线性图标",
                           line.strip()[:120]))

    has_motion = bool(MOTION.search(text))
    has_reduced = bool(REDUCED.search(text))
    has_fixed = bool(FIXED.search(text))
    has_safe = bool(SAFE_AREA.search(text))
    has_float_cue = bool(BACKDROP.search(text) or SHADOW.search(text))
    has_cv = bool(CONTENT_VIS.search(text))
    has_contain = bool(CONTAIN_SIZE.search(text))

    if has_motion and not has_reduced and not project_has_reduced:
        issues.append((0, "W1",
                       "本文件含 animation / transition，且整个扫描集合都没有 prefers-reduced-motion 降级", ""))

    if has_fixed and not has_safe:
        issues.append((0, "W2",
                       "文件含 position: fixed 但缺少 env(safe-area-inset-*) 安全区处理", ""))

    if has_fixed and not has_float_cue:
        issues.append((0, "W4",
                       "文件含 position: fixed 但既无 backdrop-filter 也无 box-shadow，浮起感不足", ""))

    if has_cv and not has_contain:
        issues.append((0, "W6",
                       "使用 content-visibility: auto 但缺少 contain-intrinsic-size（滚动条会跳变）", ""))

    return issues


def main():
    ap = argparse.ArgumentParser(description="MiniRelax 落地页红线自检（v2）")
    ap.add_argument("paths", nargs="+", help="待扫描的文件或目录")
    ap.add_argument("--quiet", action="store_true", help="仅输出汇总")
    args = ap.parse_args()

    files = sorted(set(iter_files(args.paths)))
    texts = {f: read(f) for f in files}
    project_has_reduced = any(REDUCED.search(t) for t in texts.values())

    total_e = total_w = scanned = 0

    for f in files:
        scanned += 1
        issues = find_issues(texts[f], project_has_reduced)
        if not issues:
            continue
        if not args.quiet:
            print(f"\n{f}")
        for line_no, code, msg, snippet in issues:
            sev = "ERROR" if code.startswith("E") else "WARN "
            loc = f":{line_no}" if line_no else ""
            if not args.quiet:
                print(f"  [{sev}] {code}{loc}  {msg}")
                if snippet:
                    print(f"         > {snippet}")
            if code.startswith("E"):
                total_e += 1
            else:
                total_w += 1

    print(f"\n扫描 {scanned} 个文件：{total_e} 个错误、{total_w} 个警告。")
    print("存在红线错误，请先修复再交付。" if total_e else "无红线错误。")
    print("提示：F1（低对比灰字压灰底）与 F5（flex 子项 min-width:0）需人工确认。")
    return 1 if total_e else 0


if __name__ == "__main__":
    sys.exit(main())
