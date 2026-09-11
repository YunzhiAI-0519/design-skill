# MiniRelax 落地页设计语言 Skill

> 一套可直接落地的品牌落地页设计系统：色彩 token、组件规范、完整页面结构、动效与响应式规则、九条工程红线，
> 外加可直接引用的 CSS 与红线自检脚本。给 AI 编码工具（Claude / Cursor / v0 / Copilot 等）用的"设计语言说明书"。

A brand-locked landing-page design system packaged as an Agent Skill — design tokens, component specs,
full page anatomy, motion & responsive rules, plus ready-to-use CSS and a static red-line linter.

---

## 它解决什么问题

让 AI 生成的前端页面**不跑偏**。没有这份规范时，每次生成都会得到一版风格各异的"通用 AI 风"落地页；
有了它，顶栏、Hero、内容区块、页脚、动效、响应式都收敛到同一套视觉语言，且能自动检出违反红线的写法。

设计定调：**专业、可信赖、现代 SaaS、轻微 AI 科技感、不炫技。**

## 能力范围

| 区块 | 内容 |
|---|---|
| **全局系统** | 色彩变量、渐变体系（含封面 banner 与 404/500/503 错误页）、字体排版、容器间距、点阵背景、溢出收敛 |
| **顶栏** | 悬浮胶囊导航、浅灰胶囊槽、rotate-text 翻字、mega 全宽下拉、登录态浮卡、移动端浮卡抽屉 |
| **Hero** | 点阵 + 双椭圆柔光、打字机标题、渐变字弹入、2×2 按钮阵、数据条带、深色控制台演示窗 |
| **内容区块** | 信任跑马灯 / 能力卡片 / 安全横带 / 开发者（多语言 tab）/ 定价 / 合作伙伴与案例卡 / FAQ 手风琴 / CTA 横带 |
| **页脚** | 四层结构：四列链接 → 主体双卡 → Powered by 状态行 → legal bar |
| **工程约束** | 动效白名单、`prefers-reduced-motion` 降级、响应式断点、安全区、九条红线 |

## 目录结构

```
minirelax-landing-design/
├── SKILL.md                     技能入口：用途、触发场景、工作流、红线速览
├── references/                  分模块的详细规范（按需加载）
│   ├── design-tokens.md         色彩 / 渐变 / 字体 / 容器 / 点阵 / 阴影
│   ├── components.md            按钮 / 卡片 / 徽章 / 状态点 / 溢出收敛
│   ├── nav-hero.md              顶栏 + Hero（含 mega、抽屉、演示窗）
│   ├── sections-footer.md       D1–D8 内容区块 + 页脚四层 + 数据来源
│   ├── motion-responsive.md     动效 / 断点 / 安全区 / 性能 / 可访问性
│   └── voice-and-redlines.md    文案语气 / 九条红线 / 使用模板 / 自检清单
├── assets/                      可直接引用的成品 CSS
│   ├── tokens.css               CSS 变量 + 渐变 + 工具类 + 动效降级
│   └── components.css           顶栏 / Hero / 区块 / 页脚组件样式
└── scripts/
    └── check_redlines.py        红线静态自检脚本
```

## 安装

技能目录结构与 [Agent Skills](https://github.com/anthropics/skills) 约定一致，仓库根目录即技能根目录。

```bash
# WorkBuddy
git clone https://github.com/<your-org>/minirelax-landing-design.git ~/.workbuddy/skills/minirelax-landing-design

# Claude Code / 其他兼容 Agent Skills 的工具
git clone https://github.com/<your-org>/minirelax-landing-design.git ~/.claude/skills/minirelax-landing-design
```

也可以下载 Releases 中的 `minirelax-landing-design.zip`，解压到对应的 `skills/` 目录。

## 使用

直接描述你要做的页面，技能会被自动匹配：

> 「按 MiniRelax 设计语言做一个企业级落地页」
> 「用现有视觉语言新增一个定价区块」
> 「评审这个页面是否符合我们的设计语言」

推荐用规范里的**一句话模板**驱动：

> 基于上述设计语言，为 MiniRelax 落地页新增 XX 区块/页面：遵循 A 色彩变量 + B 顶栏胶囊 + C 打字机 hero +
> D.x 对应区块样式 + E 页脚四层结构；动效与响应式遵守 A/F，红线 F 全部满足。

### 直接引用成品 CSS

```html
<link rel="stylesheet" href="assets/tokens.css" />
<link rel="stylesheet" href="assets/components.css" />
```

`tokens.css` 已包含 `prefers-reduced-motion` 降级块，`components.css` 依赖其变量，**请保持引入顺序**。

> 注意：入场动画类 `.reveal` 采用 `.js .reveal` 门控——需在 `<head>` 尽早置位：
> `<script>document.documentElement.classList.add('js');</script>`
> 这样脚本加载失败时内容依然完整可见，不会出现整页空白。

### 红线自检

```bash
python scripts/check_redlines.py ./your-output-dir
```

检出项：

| 级别 | 代码 | 检查 |
|---|---|---|
| 错误 | E1 | `transition: all` |
| 错误 | E2 | 黑色阴影（应为蓝主色系、大距离、低透明度） |
| 警告 | W1 | 缺 `prefers-reduced-motion` 降级 |
| 警告 | W2 | `position: fixed` 缺安全区处理 |
| 警告 | W3 | 用 emoji 充当功能图标 |
| 警告 | W4 | 悬浮元素浮起感不足（缺 blur / border / shadow） |
| 警告 | W5 | transition 中包含触发布局的属性 |
| 警告 | W6 | `content-visibility: auto` 缺 `contain-intrinsic-size` |

其中「低对比灰字压灰底」「flex 子项缺 `min-width: 0`」依赖语义判断，脚本无法可靠静态检出，需人工确认。

## 九条红线

1. 禁大面积低对比灰字压灰底——正文文字色不得浅于 `--text-3`
2. 禁黑色重阴影——一律「大距离 + 低透明度 + 蓝主色系」
3. 禁 `transition: all`——只过渡 `opacity / transform / border-color / color`
4. 禁直角突变——按钮 `999px` 胶囊，卡片 `≥14px`
5. 含可换行文本的 flex 子项必须 `min-width: 0`
6. 悬浮元素必须 `blur + border + shadow` 三件套
7. 移动端 fixed 底部元素必须加 `env(safe-area-inset-bottom)`
8. `content-visibility: auto` 只用于首屏外区块，且必须配 `contain-intrinsic-size`
9. 所有颜色仅来自变量表，新增色必须集中注册

## 关于品牌约束

本技能是**品牌约束型规范**，不是通用前端设计建议。当它与通用「反 AI 味」规则冲突时（例如通用建议禁用蓝紫渐变、
禁用系统字体），**一律以本品牌规范为准**。请在套用前确认你确实要遵循这套视觉语言。

## 许可

[MIT](./LICENSE) © 2026 苏州云养智健人工智能科技有限公司
