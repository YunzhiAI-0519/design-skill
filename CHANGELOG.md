# Changelog

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## v2.0.0 — 2026-09-12

从「设计 token + 组件规范」扩展为「全套页面结构」。

### 新增
- 顶栏规范：悬浮胶囊导航、浅灰胶囊槽、rotate-text 翻字、mega 全宽下拉（说明卡联动）、登录态浮卡、移动端浮卡抽屉
- Hero 规范：点阵与双椭圆柔光、打字机标题、渐变字弹入、2×2 按钮阵、数据条带、深色控制台演示窗
- D1–D8 内容区块规范（信任条 / 能力卡片 / 安全横带 / 开发者 / 定价 / 合作伙伴 / FAQ / CTA）
- 页脚四层结构 + 白标数据来源约定
- 封面 banner 四色交替渐变、404 / 500 / 503 错误页渐变
- 溢出收敛（`min-width: 0` / `overflow-wrap`）与 `content-visibility` 用法
- `scripts/check_redlines.py` 红线静态自检（8 项检查）

### 变更
- 红线由通用 9 条更新为品牌 F 九条
- `references/layout.md` 拆分为 `nav-hero.md` + `sections-footer.md`，按需加载

### 修复
- `check_redlines.py`：先剥离注释再匹配，避免注释内关键词误报为红线错误
- `check_redlines.py`：`prefers-reduced-motion` 改为项目级判断，避免多文件项目误报
- `check_redlines.py`：布局属性检查补充 `gap` / `inset*`
- `tokens.css`：`.reveal` 增加 no-js 安全兜底，脚本加载失败时内容不再空白

## v1.0.0 — 2026-09-12

首个版本：色彩系统、字体版式、组件规范、动效与响应式、必守红线。
