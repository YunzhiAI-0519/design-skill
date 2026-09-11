# A.4 通用组件语言

> 配套可引用样式：`assets/components.css`。所有交互组件都必须有 hover / focus-visible / active 三态。

| 元素 | 规范 |
|---|---|
| **按钮** | 一律胶囊 999px；主 CTA 渐变白字 hover 上浮 + 光泽扫过 + 箭头右移；副 CTA 白底描边 hover 蓝化 |
| **卡片** | 白底 `1px border`、圆角 14–20px；hover `translateY(-2~-4px)` + 主题色边框 + 蓝系大距离低透明度阴影 |
| **容器** | `max-width 1280px` 居中，区块 padding `88–96px` |
| **eyebrow** | `13px / 700 / 字距 .08em / text-3`，`dots` 装饰点可选 |
| **badge 徽章** | 22px 高胶囊：绿（无限火力）/ 橙（缓存）/ 蓝（NEW） |
| **在线点** | `#10b981` + 3px 外环 `#ecfdf5`，可 2s 呼吸动画 |
| **点阵背景** | `radial-gradient(#e4e4e7 1px, transparent 1px) 0 0/24px 24px`，opacity `.55` + 椭圆 mask 渐隐 |
| **溢出收敛** | 长词卡：`min-width:0` + `overflow-wrap:break-word`；名称行 `nowrap + ellipsis` |
| **动效** | 交互 `.15–.25s ease`；滑入 `.25–.3s cubic-bezier(.32,.72,0,1)`；回弹 `cubic-bezier(.34,1.3~1.56,.64,1)`；入场 translateY + opacity，observer 梯度 `.08/.16/.24s`；尊重 `prefers-reduced-motion`；禁 `transition:all` |
| **响应式** | `>1024` 完整 / `768–1024` 压缩 / `≤768` 汉堡单列 / 安全区 `env(safe-area-inset-bottom)` |

---

## 按钮

| 类型 | 规范 |
|---|---|
| 主 CTA | 胶囊；渐变 `--grad-cta` 白字；hover 上浮 + 光泽扫过（`::after` 位移）+ 箭头右移 |
| 副 CTA | 白底描边胶囊；hover 上浮 + 边框/文字蓝化 |
| 深色态主按钮 | `--ink` 底白字胶囊（顶栏注册 / 抽屉内），`42px` 高，hover `#1e293b` + 上浮 |
| 小链接按钮 | 白底描边 999px，hover 变蓝上浮 |

```css
.btn { border-radius: 999px; transition: transform .2s ease, background-color .2s ease,
       border-color .2s ease, color .2s ease, box-shadow .2s ease; }
.btn--primary { background-image: var(--grad-cta); color: #fff; overflow: hidden; position: relative; }
.btn--primary::after {            /* 光泽扫过 */
  content: ""; position: absolute; top: 0; bottom: 0; left: -60%; width: 45%;
  background: linear-gradient(100deg, transparent, rgba(255,255,255,.35), transparent);
  transform: skewX(-18deg); pointer-events: none;
}
.btn--primary:hover { transform: translateY(-2px); }
.btn--primary:hover::after { transform: translateX(340%) skewX(-18deg); transition: transform .6s ease; }
.btn--ink { background: var(--ink); color: #fff; height: 42px; }
.btn--ink:hover { background: #1e293b; transform: translateY(-2px); }
```

---

## 卡片

```css
.card {
  background: var(--bg); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 24px; min-width: 0;
  transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease;
}
.card:hover { transform: translateY(-3px); border-color: var(--primary-border); box-shadow: var(--shadow-card-hover); }
.card__icon-chip { width: 44px; height: 44px; border-radius: 12px; background: var(--primary-soft); }
.card__text { overflow-wrap: break-word; }
.card__name { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
```

---

## 徽章 / 序号芯片

三色语义：**绿 = 无限火力**，**橙 = 缓存**，**蓝 = NEW**。

```css
.badge { height: 22px; padding: 0 10px; border-radius: 999px; font-size: 12px; font-weight: 600; }
.badge--success { background: #ecfdf5; border: 1px solid #a7f3d0; color: var(--success); } /* 无限火力 */
.badge--warn    { background: #fffbeb; border: 1px solid #fde68a; color: var(--warn); }    /* 缓存 */
.badge--new     { background: var(--primary-soft); border: 1px solid var(--primary-border); color: var(--primary); } /* NEW */

.index-chip {                                   /* 01 02 03… */
  width: 28px; height: 28px; border-radius: 9px; display: grid; place-items: center;
  background: var(--bg-alt); color: var(--text-3); font-weight: 700; font-variant-numeric: tabular-nums;
}
.index-chip.is-active { background: var(--primary); color: #fff; }   /* FAQ 激活态 */
```

---

## 在线点 / 呼吸点

```css
.status-dot { width: 8px; height: 8px; border-radius: 50%; background: #10b981; box-shadow: 0 0 0 3px #ecfdf5; }
.status-dot--pulse { animation: dot-pulse 2s ease-in-out infinite; }
@keyframes dot-pulse { 0%,100% { transform: scale(.85); opacity: .85 } 50% { transform: scale(1.15); opacity: 1 } }
```

页脚 `STRATEGIC PARTNERSHIP` 的 **三色呼吸点**用同一动画，仅换 `background`（蓝 / 紫 / 青）。

---

## 溢出收敛（红线 5）

```css
/* flex / grid 子项：必须 min-width:0，否则长英文 id 撑爆卡片右侧 */
.flex-child { min-width: 0; }
/* 长词可断行 */
.wrap-anywhere { overflow-wrap: break-word; }
/* 名称行省略 */
.ellipsis { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
```
