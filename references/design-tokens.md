# A. 全局设计系统 — 色彩 · 渐变 · 字体 · 容器

> 本文件是品牌设计 token 的事实来源。所有页面颜色、字体、圆角、阴影都必须走这里定义的变量。
> 可直接引用的落地文件：`assets/tokens.css`。

## A1. 色彩变量

```css
--primary:#2563eb; --primary-hover:#1d4ed8; --primary-active:#1e40af;
--primary-soft:#eff6ff; --primary-border:#bfdbfe;
--ink:#0f172a;
--text-1:#0f172a; --text-2:#334155; --text-3:#64748b; --text-4:#94a3b8;
--border:#e2e8f0; --border-light:#eef2f7;
--bg:#ffffff; --bg-alt:#f8fafc; --bg-code:#0f172a;
--success:#059669; --success-soft:#ecfdf5; --warn:#d97706;
--radius-lg:16px; --radius-md:12px;
```

### 语义色

| 语义 | 主色 | 淡底 / 边框 |
|---|---|---|
| 成功 / 在线 | `--success` `#059669` | `#ecfdf5` / `#a7f3d0` |
| 提示 / 数值高亮 | `--warn` `#d97706`（高亮可用 `#f59e0b`） | `#fffbeb` / `#fde68a` |
| 新品 / 主推 | `--primary` `#2563eb` | `--primary-soft` / `--primary-border` |

> 红线第 9 条：**所有颜色仅来自本变量表；需要新增色先在 A1 注册。** 禁止在组件里直接写十六进制色值。

---

## A2. 渐变体系（点睛用）

```css
/* 品牌副标 / CTA：indigo → blue → cyan */
--grad-cta: linear-gradient(90deg, #4f46e5, #2563eb, #0891b2);

/* 品牌辅：蓝 → 紫 */
--grad-brand: linear-gradient(135deg, #2563eb, #7c3aed);

/* 封面 banner 交替四色（案卡 / logo 墙封面轮换用） */
--grad-banner-a: linear-gradient(135deg, #2563eb, #7c3aed);  /* 蓝紫 */
--grad-banner-b: linear-gradient(135deg, #0891b2, #2563eb);  /* 青蓝 */
--grad-banner-c: linear-gradient(135deg, #4f46e5, #c026d3);  /* 紫粉 */
--grad-banner-d: linear-gradient(135deg, #0284c7, #4f46e5);  /* 湛蓝 */

/* 错误页 */
--grad-404: linear-gradient(135deg, #2563eb, #7c3aed);            /* 蓝 → 紫 */
--grad-500: linear-gradient(135deg, #d97706, #dc2626, #db2777);   /* 橙 → 红 → 粉 */
--grad-503: linear-gradient(135deg, #2563eb, #7c3aed);            /* 维护：蓝紫 */
```

使用约束：
- 渐变只用于 **CTA 按钮、Hero 渐变字、封面 banner、FAQ 左侧粘性卡、cta-band、错误页** 等点缀位。
- 不用于大面积背景铺底，不用于普通正文或小图标。
- 封面 banner 四色按顺序**交替轮换**使用，避免整页单色。

---

## A3. 字体与排版

```css
--font-sans: "PingFang SC", "Microsoft YaHei", system-ui, -apple-system,
             "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

> 本品牌**有意使用系统字体栈、中文优先**。与通用「禁用系统字体」建议冲突时以品牌为准，不要替换为展示字体。

| 角色 | 规格 |
|---|---|
| 大标题（H1 / Hero） | `font-weight: 800–900`、`letter-spacing: -0.02em`、`line-height: 1.1–1.15` |
| 英文点缀 | `10–11px`、`600`、`letter-spacing: .1–.12em`、`uppercase`、颜色 `--text-4` |
| 数字 | 一律 `font-variant-numeric: tabular-nums` |

### 眼眉（eyebrow）双规格说明

v2 中眼眉出现在两处语境，规格略有差异，**按语境二选一，不要混用**：

| 语境 | 规格 |
|---|---|
| A.4 通用轻量标签 | `13px / 700 / letter-spacing .08em / 颜色 --text-3`，可选 `dots` 装饰点 |
| D 内容区 section 标题眉标 | `12px / 700 / letter-spacing .1em / 大写 / 颜色 --primary` |

> 建议：section 标题统一用「12px 蓝大写」，其他轻量标签用「13px text-3」。

---

## A4. 容器与间距

| 项目 | 值 |
|---|---|
| 内容容器 | `max-width: 1280px`（Tailwind `max-w-7xl`）居中 |
| 区块纵向 padding | `88–96px`（桌面） |
| 栅格间距 | `16 / 24 / 32px` |
| 卡片内边距 | `20–28px` |

---

## A5. 点阵背景

```css
background-image: radial-gradient(#e4e4e7 1px, transparent 1px);
background-size: 24px 24px;
background-position: 0 0;
opacity: .55;
/* 配椭圆 mask 渐隐，避免硬边 */
-webkit-mask-image: radial-gradient(ellipse at 50% 40%, #000 30%, transparent 75%);
        mask-image: radial-gradient(ellipse at 50% 40%, #000 30%, transparent 75%);
```

---

## A6. 圆角与阴影家族

### 圆角

| 元素 | 圆角 |
|---|---|
| 按钮 / 徽章 | `999px` |
| 卡片 | `14–20px`（`--radius-lg` 16 / `--radius-md` 12） |
| logo 芯片 | `8px`（32px 方） |
| 图标方块 | `10–14px` 或 `50%`（圆） |
| 输入框 / 序号芯片 | `10px` 左右 |

### 阴影（一律蓝主色系，大距离 + 低透明度）

```css
--shadow-card-hover: 0 12px 32px rgba(37, 99, 235, .10);
--shadow-panel:      0 8px 26px rgba(37, 99, 235, .08);
--shadow-float:      0 8px 30px rgba(15, 23, 42, .08), 0 2px 8px rgba(15, 23, 42, .04);
--shadow-nav:        0 6px 24px rgba(15, 23, 42, .06), 0 2px 8px rgba(15, 23, 42, .04);
--shadow-fab:        0 6px 18px rgba(15, 23, 42, .10), 0 2px 6px rgba(15, 23, 42, .06);
```

> 红线第 2 条：**禁黑色重阴影**。阴影必须是低透明度（`.04–.14`）+ 较大 blur 的蓝主色系。

---

## A7. 溢出收敛（长文本防撑爆）

长词卡片必须收敛溢出，否则长英文 id / 无空格字符串会撑爆右侧：

```css
.card, .card__body { min-width: 0; }                 /* flex/grid 子项 */
.card__text       { overflow-wrap: break-word; }     /* 长词可断行 */
.card__name       { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
```

> 红线第 5 条：**含可换行文本的 flex 子项必须 `min-width: 0`。**
