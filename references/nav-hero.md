# B. 顶栏（悬浮胶囊导航） + C. Hero

---

# B. 顶栏

## B1. 定位与吸顶

- 导航**不占通栏**：`position: absolute; top: 14px`，浮于 hero 上层。
- 滚动 `> 8px` 后加 `.fixed-in` → `position: fixed` 吸顶（可同步收紧内边距）。

```css
.topbar {
  position: absolute; top: 14px; left: 50%; transform: translate(-50%, 0);
  width: min(1200px, calc(100% - 32px)); height: 64px;
  display: flex; align-items: center; gap: 16px; padding: 0 12px 0 20px;
  background: rgba(255, 255, 255, .82);
  -webkit-backdrop-filter: blur(16px); backdrop-filter: blur(16px);
  border: 1px solid rgba(226, 232, 240, .7);
  border-radius: 999px;
  box-shadow: var(--shadow-nav);
  z-index: 70;
  /* 只过渡 transform / box-shadow / background-color，避免布局抖动（红线 3） */
  transition: transform .25s ease, box-shadow .25s ease, background-color .25s ease;
}
/* 吸顶「收紧」用位移 + 更强阴影 / 更实底色表达，尺寸保持不变 */
.topbar.fixed-in {
  position: fixed; top: 14px;
  transform: translate(-50%, -6px);
  background: rgba(255, 255, 255, .92);
  box-shadow: var(--shadow-float);
}
```

> 注意：滚动「收紧」若用 `top / height / padding` 过渡会触发布局重排（违反红线 3）。
> 用 `transform + box-shadow + background-color` 表达同样的视觉层级变化，尺寸保持不变。

## B2. 结构分区

| 位置 | 内容 |
|---|---|
| 左 | 圆角 logo 芯片（`32px`、圆角 `8px`）+ 品牌名 `18px / 700` |
| 中 | 导航链接嵌在**浅灰胶囊槽**内 |
| 右 | 登录文字链 + **深色胶囊注册主按钮**（`--ink` 底、`42px` 高、hover `#1e293b` 上浮） |

```css
.topbar__slot {                    /* 浅灰胶囊槽 */
  display: flex; align-items: center; gap: 4px; padding: 4px;
  background: rgba(241, 245, 249, .75);
  border: 1px solid var(--border-light);
  border-radius: 999px;
}
.topbar__link {
  padding: 8px 14px; border-radius: 999px; color: var(--text-2);
  transition: background-color .2s ease, color .2s ease, box-shadow .2s ease, transform .2s ease;
}
.topbar__link:hover { background: #fff; box-shadow: var(--shadow-panel); transform: translateY(-1px); }
.topbar__link.is-active { color: var(--primary); background: #fff; box-shadow: var(--shadow-panel); }
```

## B3. 兜底动效：rotate-text 翻字 + 短下划线

- 翻字：`.rt span::after { content: attr(data-title) }`，hover 时原字上移出、蓝字从下滑入（`.4s`）。
- 下划线：底部 `16px` 短下划线从中心展开（`::after` 宽 `0 → 16px`）。

```css
.rt { position: relative; display: inline-block; overflow: hidden; }
.rt span { display: block; transition: transform .4s cubic-bezier(.32,.72,0,1); }
.rt span::after {
  content: attr(data-title); position: absolute; left: 0; top: 100%;
  color: var(--primary); white-space: nowrap;
}
.rt:hover span { transform: translateY(-100%); }

/* 视觉上是「0 → 16px 展开」，但用 scaleX 实现以免过渡布局属性（红线 3） */
.nav-underline { display: block; height: 2px; width: 16px; margin: 0 auto; background: var(--primary);
  transform: scaleX(0); transform-origin: center; transition: transform .2s ease; }
.nav-link:hover .nav-underline { transform: scaleX(1); }
```

## B4. 登录态

- 蓝色渐变 `30px` 圆头像 + 用户名胶囊。
- 点击展开**下拉浮卡**：余额渐变块 + 控制台 / 账户设置 / 退出登录（红色项）。

```css
.user-pill { display: inline-flex; align-items: center; gap: 8px; height: 38px; padding: 0 12px 0 4px;
  background: var(--bg-alt); border: 1px solid var(--border-light); border-radius: 999px; cursor: pointer; }
.user-avatar { width: 30px; height: 30px; border-radius: 50%; background: var(--grad-brand); color: #fff;
  display: grid; place-items: center; font-size: 13px; font-weight: 700; }
.user-menu { position: absolute; top: calc(100% + 10px); right: 0; width: 240px; padding: 8px;
  background: #fff; border: 1px solid var(--border-light); border-radius: var(--radius-md); box-shadow: var(--shadow-float); }
.user-menu__balance { background: var(--grad-brand); color: #fff; border-radius: var(--radius-md); padding: 14px 16px; }
.user-menu__item { display: flex; align-items: center; height: 40px; padding: 0 12px; border-radius: 10px; color: var(--text-2); }
.user-menu__item:hover { background: var(--bg-alt); }
.user-menu__item--danger { color: #dc2626; }   /* 退出登录 */
```

## B5. 移动端

- 汉堡按钮放在胶囊内。
- 展开**浮卡抽屉**：`top: 76px`、左右 `12px` 缩进、圆角 `24px`、白 `97%` + blur；
  内部顺序：蓝紫渐变用户卡 → 圆角菜单行 → 胶囊双按钮。

```css
.nav-drawer {
  position: fixed; top: 76px; left: 12px; right: 12px; border-radius: 24px;
  background: rgba(255, 255, 255, .97);
  -webkit-backdrop-filter: blur(16px); backdrop-filter: blur(16px);
  border: 1px solid var(--border-light); box-shadow: var(--shadow-float);
  padding: 12px 12px calc(12px + env(safe-area-inset-bottom));
  z-index: 75;
}
.nav-drawer__user { background: var(--grad-brand); color: #fff; border-radius: 16px; padding: 16px; }
```

## B6. mega 全宽下拉（配置驱动）

- hover 导航项触发 `fixed` 面板：`left: 0; right: 0; top: 96px`。
- 左 `300px` 说明卡（**跟随所悬停子项联动切换**）+ 右 `3` 列分组链接（`h5` 带蓝色竖条 `::before`）。
- 白底大投影。

```css
.mega { position: fixed; left: 0; right: 0; top: 96px; background: #fff; box-shadow: var(--shadow-float);
  border-top: 1px solid var(--border-light); opacity: 0; visibility: hidden; transition: opacity .25s ease, transform .25s ease; transform: translateY(-6px); }
.mega.is-open { opacity: 1; visibility: visible; transform: none; }
.mega__inner { max-width: 1280px; margin-inline: auto; display: grid; grid-template-columns: 300px 1fr 1fr 1fr; gap: 32px; padding: 32px 24px; }
.mega h5 { position: relative; padding-left: 12px; }
.mega h5::before { content: ""; position: absolute; left: 0; top: .2em; bottom: .2em; width: 3px; border-radius: 2px; background: var(--primary); }
.mega__aside { position: sticky; top: 0; align-self: start; }
```

> mega 内容应由配置（导航数据）驱动，不要硬编码在组件里。

---

# C. Hero 区

## C1. 容器

- `padding: 96px 0 72px`（移动端顶部 `108px`，避开胶囊顶栏与公告）。
- 白背景 + 点阵纹理 + 左右上双椭圆柔光（`radial-gradient rgba(59,130,246,.14)`、紫色 `.12`）。

```css
.hero {
  position: relative;
  padding: 96px 0 72px;
  background-image: radial-gradient(#e4e4e7 1px, transparent 1px);
  background-size: 24px 24px;
}
.hero::before {                       /* 点阵椭圆渐隐 + 双色柔光 */
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background:
    radial-gradient(600px 320px at 18% 12%, rgba(59, 130, 246, .14), transparent 70%),
    radial-gradient(520px 300px at 82% 10%, rgba(124, 58, 237, .12), transparent 70%),
    radial-gradient(ellipse at 50% 45%, transparent 30%, var(--bg) 78%);
}
@media (max-width: 768px) { .hero { padding-top: 108px; } }
```

## C2. 层级序列与层叠动效

顺序（reveal 梯度依次触发）：

```
① NEW 徽章（可选）→ ② 打字机 H1 → ③ .hero-grad-line 渐变字（.25s 后弹入）
→ ④ CTA / 入口卡 → ⑤ hero-stats → ⑥ 控制台演示窗
```

### ① NEW 徽章

白底胶囊槽 + 左侧 `primary-soft` 小 `NEW` 标签。

```css
.hero-badge { display: inline-flex; align-items: center; gap: 10px; height: 34px; padding: 4px 14px 4px 4px;
  background: #fff; border: 1px solid var(--border-light); border-radius: 999px; box-shadow: var(--shadow-panel); }
.hero-badge__tag { height: 26px; padding: 0 10px; display: grid; place-items: center;
  background: var(--primary-soft); color: var(--primary); border-radius: 999px; font-size: 11px; font-weight: 700; letter-spacing: .08em; }
```

### ② 打字机 H1 + ③ 渐变字弹入

- 打字机：`一个 API，` 逐字 `110ms` + `caret`（`4px` 黑色、`steps(1)` 闪烁）。
- 完成后 `.hero-grad-line`「接入所有模型」渐变字弹入：`translateY(14px) → 0`、
  `cubic-bezier(.34,1.3,.64,1)`、`background-clip: text`（indigo→blue→cyan）。**仅过渡 `opacity / transform`。**

```css
.typewriter__caret { display: inline-block; width: 4px; height: 1em; background: #0f172a; vertical-align: -.1em;
  animation: caret-blink 1s steps(1) infinite; }
@keyframes caret-blink { 0%,50% { opacity: 1 } 51%,100% { opacity: 0 } }

.hero-grad-line {
  display: block;
  background: var(--grad-cta);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent; color: transparent;
  opacity: 0; transform: translateY(14px);
  animation: grad-line-in .5s cubic-bezier(.34, 1.3, .64, 1) .25s forwards;
}
@keyframes grad-line-in { to { opacity: 1; transform: none; } }
```

### ④ 副文案

`16px`、`--text-3`；关键短语 `white-space: nowrap`，用 `<br>` 控制换行节奏。

### ⑤ 2×2 双栏按钮阵（`max-width: 640px`）

| 位置 | 内容 |
|---|---|
| 渐变主 CTA | 胶囊；内部**双行**（主标题 `800` + `11px` 小字）；右箭头 hover 右移；扫光 |
| 白描边副 CTA | 双行（中文 + `uppercase` 英文小标签） |
| 两张入口卡 | 圆角 `18px` 白卡 = 圆形图标芯片 `42px` + 中英文双行 + 折角 chevron；蓝 / 紫双色 hover |

```css
.hero__actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; max-width: 640px; margin-top: 32px; }
.hero-entry { display: flex; align-items: center; gap: 12px; padding: 14px 16px; background: #fff;
  border: 1px solid var(--border); border-radius: 18px; min-width: 0;
  transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease; }
.hero-entry:hover { transform: translateY(-2px); box-shadow: var(--shadow-panel); }
.hero-entry--blue:hover { border-color: var(--primary-border); }
.hero-entry--violet:hover { border-color: #ddd6fe; }
.hero-entry__chip { width: 42px; height: 42px; border-radius: 50%; display: grid; place-items: center; flex: none;
  background: var(--primary-soft); color: var(--primary); }
.hero-entry--violet .hero-entry__chip { background: #f5f3ff; color: #7c3aed; }
.hero-entry__chevron { margin-left: auto; transition: transform .2s ease; }
.hero-entry:hover .hero-entry__chevron { transform: translateX(3px); }
@media (max-width: 640px) { .hero__actions { grid-template-columns: 1fr; } }
```

### ⑥ hero-stats（2×2 数据条带）

单边框圆角、四格；每格右上 `num`（`800`）+ `em` 单位小字、`label` `12.5px` 灰。移动端 `2` 列。

```css
.hero-stats { display: grid; grid-template-columns: repeat(4, 1fr); margin-top: 40px;
  border: 1px solid var(--border); border-radius: var(--radius-lg); overflow: hidden; }
.hero-stats__cell { padding: 18px 20px; border-right: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light); min-width: 0; }
.hero-stats__num { font-size: 26px; font-weight: 800; color: var(--text-1); font-variant-numeric: tabular-nums; }
.hero-stats__num em { font-size: 12px; font-weight: 600; color: var(--text-3); font-style: normal; margin-left: 4px; }
.hero-stats__label { font-size: 12.5px; color: var(--text-3); }
@media (max-width: 768px) { .hero-stats { grid-template-columns: repeat(2, 1fr); } }
```

### ⑦ 控制台演示窗

`macOS` 三点 bar + 深色 `--bg-code` **双 pane**（`Request` / `Response · stream`，动态注入文字 + 闪烁竖条光标）
+ 底部 chips（`OpenAI 兼容` / `Anthropic 兼容` / `SSE 流式` / `Function Calling`）。

```css
.demo { margin-top: 40px; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid #1e293b; box-shadow: var(--shadow-float); }
.demo__bar { display: flex; align-items: center; gap: 6px; height: 40px; padding: 0 14px; background: #111827; }
.demo__dot { width: 11px; height: 11px; border-radius: 50%; }
.demo__body { display: grid; grid-template-columns: 1fr 1fr; background: var(--bg-code); color: #e2e8f0; }
.demo__pane { padding: 18px; font: 12.5px/1.7 ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; min-width: 0; overflow-wrap: break-word; }
.demo__pane + .demo__pane { border-left: 1px solid #1e293b; }
.demo__caret { display: inline-block; width: 2px; height: 1.05em; background: #38bdf8; vertical-align: -.15em; animation: caret-blink 1s steps(1) infinite; }
.demo__chips { display: flex; flex-wrap: wrap; gap: 8px; padding: 14px; background: var(--bg-code); border-top: 1px solid #1e293b; }
.demo__chip { height: 26px; padding: 0 10px; display: inline-flex; align-items: center; border-radius: 999px;
  font-size: 11px; font-weight: 600; color: #cbd5e1; background: rgba(148, 163, 184, .12); border: 1px solid rgba(148, 163, 184, .2); }
@media (max-width: 768px) { .demo__body { grid-template-columns: 1fr; } .demo__pane + .demo__pane { border-left: 0; border-top: 1px solid #1e293b; } }
```

---

## C3. 补充：客服悬浮组件（沿用 v1，属站点 chrome）

右侧圆形白卡逐个分离（`52px` 圆、双层投影），点击弹出抽屉或 kkidc tooltip；移动端 `40px`；
**底部必须避开安全区**。

```css
.fab-stack { position: fixed; right: 20px; bottom: calc(24px + env(safe-area-inset-bottom));
  display: flex; flex-direction: column; gap: 12px; z-index: 60; }
.fab { width: 52px; height: 52px; border-radius: 50%; background: #fff; box-shadow: var(--shadow-fab);
  display: grid; place-items: center; transition: transform .2s ease, box-shadow .2s ease; }
.fab:hover { transform: translateY(-2px); box-shadow: 0 10px 26px rgba(37, 99, 235, .16); }
@media (max-width: 768px) { .fab { width: 40px; height: 40px; } }
```
