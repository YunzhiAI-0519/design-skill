# 动效 · 响应式 · 性能 · 可访问性

## 一、动效规则

| 场景 | 时长 / 缓动 |
|---|---|
| 交互（hover / 状态切换） | `.15–.25s ease` |
| 面板滑入（抽屉 / mega / 浮卡） | `.25–.3s cubic-bezier(.32,.72,0,1)` |
| 弹性回弹 | `cubic-bezier(.34,1.3~1.56,.64,1)` |
| 翻字 / 打字机 | `.4–.5s` |
| 光标闪烁 | `steps(1)`（硬切） |

```css
--ease-slide:  cubic-bezier(.32, .72, 0, 1);     /* 品牌主缓动 */
--ease-spring: cubic-bezier(.34, 1.3, .64, 1);   /* 回弹 */
```

### 可过渡属性白名单（红线 3）

**只允许过渡：`opacity` / `transform` / `border-color` / `color`。**

- 禁止 `transition: all`。
- 不要过渡 `width / height / top / left / margin / padding / font-size` 等布局属性；
  需要尺寸变化时用 `transform: scale()` 或 `clip-path`。

```css
/* ✅ */ transition: transform .2s ease, border-color .2s ease, color .2s ease, opacity .2s ease;
/* ❌ */ transition: all .2s ease;
```

### 入场动画（observer 梯度）

- `translateY + opacity`，由 `IntersectionObserver` 加 `.in` 触发。
- 延迟梯度 `.08s / .16s / .24s`（`calc(var(--i) * 80ms)`）。

```css
/* 安全兜底：无 JS 时默认可见；仅在 <html class="js"> 时才隐藏等待入场。
   若脚本加载失败而 .reveal 仍为 opacity:0，整页会变空白 —— 必须加这层保护。 */
.reveal { opacity: 1; transform: none; }
.js .reveal { opacity: 0; transform: translateY(16px); }
.js .reveal.in {
  opacity: 1; transform: none;
  transition: opacity .5s ease-out, transform .5s ease-out;
  transition-delay: calc(var(--i, 0) * 80ms);
}
```

在 `<head>` 最前面加一行，尽早置位 `.js`（避免闪烁）：

```html
<script>document.documentElement.classList.add('js');</script>
```

```js
const io = new IntersectionObserver((entries) => {
  for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach((el, i) => { el.style.setProperty('--i', i % 4); io.observe(el); });
```

### Hero 层叠动效顺序

```
badge → H1 打字机 → .hero-grad-line（.25s 后）→ CTA / 入口卡 → hero-stats → demo
```

### 降级（红线必查）

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
  .reveal { opacity: 1; transform: none; }
  .marquee__row { animation: none; }        /* 跑马灯停止 */
}
```

> 打字机、渐变字弹入、呼吸点、翻字、跑马灯、视差——全部必须在此降级。

---

## 二、性能：content-visibility（红线 8）

首屏外的内容区块用 `content-visibility: auto` 跳过渲染，**必须**配 `contain-intrinsic-size` 占位，
否则滚动条会跳变：

```css
.below-the-fold {
  content-visibility: auto;
  contain-intrinsic-size: 720px;
}
```

- 只用于**首屏外**的区块。
- 不要用在首屏 Hero、顶栏、粘性 FAQ 卡上。

---

## 三、响应式断点

| 断点 | 处理 |
|---|---|
| `>1024px` | 完整布局 |
| `768–1024px` | 压缩版：导航收窄、二级链接隐藏、网格降列 |
| `≤768px` | 汉堡单列；顶栏浮卡抽屉 `top: 76px`；Hero 顶部 padding `108px` |
| 安全区 | 底部 `env(safe-area-inset-bottom)` 全适配 |

### 安全区清单（移动端必查）

所有 `position: fixed` / 贴底元素都要处理：

```css
padding-bottom: env(safe-area-inset-bottom);
/* 或 */ bottom: calc(24px + env(safe-area-inset-bottom));
```

检查项：客服悬浮组件、导航浮卡抽屉、侧滑抽屉、底栏 CTA、Toast、页脚 legal bar。

---

## 四、可访问性下限

- 正文对比度 ≥ `4.5:1`，大字 ≥ `3:1`。
  红线 1：**禁大面积低对比灰字压灰底**——正文文字色不得浅于 `--text-3`（`#64748b`）。
- 触摸目标 ≥ `44×44px`。
- 所有可交互元素有可见 `:focus-visible` 态（用 `outline`，不要只靠 `box-shadow`）。
- 语义化标签 + 键盘可达 + 动态内容 `aria-live="polite"`。
- 自动播放动画（跑马灯 / 打字机）提供暂停入口，并响应 `prefers-reduced-motion`。
