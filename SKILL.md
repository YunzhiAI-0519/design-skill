---
name: minirelax-landing-design
description: MiniRelax 品牌落地页视觉语言与实现规范（v2 全景版）。当需要按该品牌现有视觉语言设计、移植、续写或重做落地页 / 官网首页 / 营销活动页，生成符合其配色、顶栏、Hero、内容区块、页脚、动效、响应式规范的 HTML/CSS/React/Vue 代码，或评审现有页面是否符合该设计语言时使用。触发场景包括「MiniRelax 落地页」「MiniRelax 设计语言」「按现有视觉语言续作新页面」「落地页改版对齐设计系统」「按设计 token 出区块」等。
agent_created: true
---

# MiniRelax 落地页设计语言 · v2（全景）

## Overview

本技能封装 MiniRelax 品牌落地页的完整设计语言（Design System）：全局系统（色彩 / 渐变 / 字体 / 通用组件语言）、
顶栏、Hero、八类内容区块、页脚四层、动效与响应式、九条红线，并附带可直接引用的 CSS token、组件样式与红线自检脚本。

用途：任意一次「按 MiniRelax 视觉语言做落地页」的工作，都产出风格一致、可直接落地、不跑偏的代码。

一句话定调：**专业、可信赖、现代 SaaS、轻微 AI 科技感、不炫技。**

## 何时使用

使用：新做 / 移植 / 续写 MiniRelax 落地页、官网首页、活动页；与该品牌保持视觉一致的前端页面；
评审页面是否偏离设计语言；需要品牌 token、组件样式、区块骨架。

不使用：与 MiniRelax 无关的通用页面设计；非视觉任务。

## 最关键的一条：品牌规范优先于通用反套路规则

通用前端方法论（禁蓝紫渐变、禁系统字体、禁纯黑并禁用渐变文字等）是**通用建议**；
本技能是**品牌约束型规范**。冲突时**一律以品牌规范为准**：

| 冲突点 | 通用建议 | 本品牌规定（优先） |
|---|---|---|
| 主色 / 渐变 | 禁用 AI 蓝紫 | 主蓝 `#2563eb`；CTA indigo→blue→cyan；辅渐变 蓝→紫 |
| 字体 | 禁用系统字体 | 系统字体栈，中文优先（PingFang SC / Microsoft YaHei） |
| 阴影 | — | **只用蓝主色系「大距离 + 低透明度」**，禁黑色重阴影 |
| 圆角 | 自由 | 按钮胶囊 999px；卡片 ≥14px |
| 强调色 | 单一强调色 | 主题蓝紫一套 + cyan/orange 徽章点缀；禁引入新主色 |

不要把品牌蓝换成别的颜色、把系统字体换成展示字体——那是跑偏，不是优化。
可优化的只有：细节精度、间距节奏、动效编排、可访问性、代码质量。

## 页面全貌（一页流）

| 区块 | 要点 | 详见 |
|---|---|---|
| **B 顶栏** | 悬浮胶囊（不占通栏，`absolute top:14px`，滚动 >8px 转 `fixed` 吸顶）；浅灰胶囊导航槽；翻字 + 短下划线；深色注册按钮；登录态下拉浮卡；移动端浮卡抽屉；配置驱动 mega 全宽下拉 | `references/nav-hero.md` |
| **C Hero** | 点阵 + 双椭圆柔光；NEW 徽章 → 打字机 H1 → 渐变字弹入 → 2×2 按钮阵 → hero-stats 2×2 → 深色控制台演示窗（双 pane + 流式光标） | `references/nav-hero.md` |
| **D 内容区** | D1 信任条跑马灯 / D2 features / D3 security-band / D4 developers（curl·python·node 三 tab）/ D5 pricing / D6 partners（logo 墙 + 案例卡）/ D7 faq（左粘性渐变卡 + 右序号手风琴）/ D8 cta-band | `references/sections-footer.md` |
| **E 页脚** | 四层：四列链接 → 主体双卡（🇨🇳/🇭🇰 + 三色呼吸点）→ Powered by 状态行 → 浅灰 legal bar | `references/sections-footer.md` |

统一 section 节奏（交替 `section-alt` 浅灰）：`eyebrow → H2(36px/800) → 副文案(17px text-3)`。

## 数据驱动与白标

页脚（及导航 / 公告）数据来自 `/api/v1/site-config`：

- 字段：`footer_entity_*`、`footer_slogan`、`footer_powered_by`、`footer_address` / `footer_email` / `footer_phone`、`site_icp`
- **空值时对应元素自动 `hidden`**，不渲染空壳
- 白标场景下文案全部走该接口，禁止在组件里硬编码品牌信息

## 工作流

### Step 1 — 定调与约束确认
确认页面类型、目标受众、要复用的既有区块。声明本次使用的 token，不做「重定义品牌色」这类越界动作。

### Step 2 — 读取规范（不要凭记忆发明已写死的规范）
- 全局系统（色彩 / 渐变 / 字体 / 容器 / 通用组件语言）→ `references/design-tokens.md`、`references/components.md`
- 顶栏与 Hero → `references/nav-hero.md`
- 内容区块与页脚 → `references/sections-footer.md`
- 动效 / 响应式 / 性能 → `references/motion-responsive.md`
- 文案语气 / 九条红线 / 使用模板 → `references/voice-and-redlines.md`

直接引用现成 CSS：`assets/tokens.css`（变量 + 渐变 + 工具类）、`assets/components.css`（组件与区块样式）。

### Step 3 — 结构先行
按页面全貌搭骨架：顶栏 → Hero → 按需选 D1–D8 → cta-band → 页脚 → 悬浮组件。先出语义化 DOM 与 class 钩子。

### Step 4 — 视觉实现
颜色只走变量；圆角 / 阴影 / 动效时长只用规范值；每个交互元素具备 hover / focus-visible / active 三态。
**带可换行文本的 flex 子项必须 `min-width: 0`**（否则长英文 id 撑爆卡片）。

### Step 5 — 动效编排
按 `references/motion-responsive.md` 做一次编排好的入场序列（badge → H1 → 渐变行 → CTA → stats → demo）。
只过渡 `opacity / transform / border-color / color`，**禁 `transition: all`**；必须做 `prefers-reduced-motion` 降级。

### Step 6 — 自检与交付
跑 `scripts/check_redlines.py` + 红线清单，交付：调性说明 + 可运行代码 + token 引用方式 + 动效说明 + 响应式/安全区说明。

## 关键数值速查

| 项目 | 值 |
|---|---|
| 主蓝 / hover / active | `#2563eb` / `#1d4ed8` / `#1e40af` |
| 主蓝淡底 / 边框 | `#eff6ff` / `#bfdbfe` |
| 深墨 / 代码底 | `#0f172a`（`--ink` / `--bg-code` 同值） |
| 文字层级 | `#0f172a` / `#334155` / `#64748b` / `#94a3b8` |
| 背景 / 交替浅灰 | `#ffffff` / `#f8fafc` |
| 容器 | `max-width: 1280px` 居中；区块纵向 padding `88–96px` |
| 圆角 | 按钮 999px · 卡片 14–20px（`--radius-lg` 16 / `--radius-md` 12） |
| CTA 渐变 | `linear-gradient(90deg,#4f46e5,#2563eb,#0891b2)` |
| 辅渐变 | `linear-gradient(135deg,#2563eb,#7c3aed)` |
| 点阵 | `radial-gradient(#e4e4e7 1px, transparent 1px) 0 0/24px 24px`，opacity .55 + 椭圆 mask 渐隐 |
| 在线点 | `#10b981` + `0 0 0 3px #ecfdf5`，2s 呼吸 |
| 大标题 | 800–900 / `-0.02em` / 行高 1.1–1.15 |
| 数字 | `font-variant-numeric: tabular-nums` |
| 动效 | 交互 `.15–.25s`；滑入 `.25–.3s cubic-bezier(.32,.72,0,1)`；回弹 `cubic-bezier(.34,1.3~1.56,.64,1)` |

## 九条红线（详见 voice-and-redlines.md）

1. 禁大面积低对比灰字压灰底——文字色 ≥ `--text-3`。
2. 禁黑色重阴影——一律「大距离 + 低透明度 + 蓝主色系」。
3. 禁 `transition: all`——只过渡 `opacity / transform / border-color / color`。
4. 禁直角突变——按钮 999px 胶囊，卡片 ≥14px。
5. 含可换行文本的 flex 子项必须 `min-width: 0`，否则长英文 id 撑爆卡片。
6. 悬浮元素（nav / notice / mega / 抽屉）必须 `blur + border + shadow` 三件套，禁贴面出现。
7. 移动端 fixed 底部元素必须加 `env(safe-area-inset-bottom)`。
8. `content-visibility: auto` 只用于首屏外区块，且必须配 `contain-intrinsic-size: 720px`。
9. 所有颜色仅来自变量表；新增色必须先在 A.1 注册。

## 一句话使用模板（G）

> 「基于上述设计语言，为 MiniRelax 落地页新增 XX 区块/页面：遵循 A 色彩变量 + B 顶栏胶囊 + C 打字机 hero +
> D.x 对应区块样式 + E 页脚四层结构；动效与响应式遵守 A/F，红线 F 全部满足；白标文案走 `/api/v1/site-config`。」

## 资源索引

- `references/design-tokens.md` — A 全局系统：色彩变量、渐变体系（含封面 banner 与 404/500/503 错误页）、字体排版、容器间距
- `references/components.md` — A.4 通用组件语言：按钮、卡片、eyebrow、徽章、在线点、点阵、溢出收敛
- `references/nav-hero.md` — B 顶栏 + C Hero
- `references/sections-footer.md` — D1–D8 内容区块 + E 页脚四层 + site-config
- `references/motion-responsive.md` — 动效、响应式、性能、可访问性
- `references/voice-and-redlines.md` — 文案语气、九条红线、使用模板、交付自检清单
- `assets/tokens.css` — 可直接引用的 CSS 变量 + 渐变 + 工具类
- `assets/components.css` — 顶栏 / Hero / 区块 / 页脚组件基础样式
- `scripts/check_redlines.py` — 红线静态自检

## 常见错误

- 用通用「反 AI 味」规则推翻品牌色 / 字体 → **跑偏**。
- 硬编码色值、新增未注册颜色 → 后续无法统一改版。
- 黑阴影、直角按钮、`transition: all`、缺 `min-width: 0` → 直接违反红线。
- 悬浮元素缺 blur+border+shadow → 无层次贴面。
- 移动端 fixed 元素压住手势条 → 未处理安全区。
- 页脚空字段仍渲染空壳 → 未按 site-config 空值 hidden 规则处理。
- 用 emoji 充当功能图标 → 应改 SVG 线性图标。
