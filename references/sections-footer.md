# D. 内容区块（D1–D8） + E. 页脚

## 统一的 section 节奏

```
eyebrow（12px 蓝大写）→ H2（36px / 800）→ 副文案（17px text-3）
```

区块交替使用 `.section-alt`（`background: var(--bg-alt)`）形成浅灰节奏；区块纵向 padding `88–96px`。

```css
.section { padding: 88px 0; }
.section-alt { background: var(--bg-alt); }
.section__eyebrow { font-size: 12px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--primary); }
.section__title { font-size: 36px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.15; color: var(--text-1); }
.section__desc { font-size: 17px; color: var(--text-3); max-width: 62ch; }
```

---

## D1. 信任条（trust）

白底分隔条：标题左 + **双行 marquee 跑马灯**（logo 灰底 chip 反向无限滚动，两端 mask 渐隐，hover 暂停）。

```css
.marquee { overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent);
                                        mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent); }
.marquee__row { display: flex; gap: 12px; width: max-content; animation: marquee-l 28s linear infinite; }
.marquee__row--reverse { animation-name: marquee-r; }
.marquee:hover .marquee__row { animation-play-state: paused; }
@keyframes marquee-l { to { transform: translateX(-50%); } }
@keyframes marquee-r { from { transform: translateX(-50%); } to { transform: none; } }

.trust-chip { height: 44px; padding: 0 18px; display: inline-flex; align-items: center; gap: 8px;
  background: var(--bg-alt); border: 1px solid var(--border-light); border-radius: 10px; color: var(--text-3); font-weight: 600; }
@media (prefers-reduced-motion: reduce) { .marquee__row { animation: none; } }
```

---

## D2. features（产品能力）

3 列卡片（`>1024px` 为 4 列布局、可转 2×2 wide）。每卡：

- 顶部**图标方块** `40px`（`primary-soft` 圆角、图标蓝）
- 标题 `16.5px` / 描述 `14.5px`
- **3 条勾选点**（✓ 蓝勾 + 灰字小项）

```css
.features { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.feature__icon { width: 40px; height: 40px; border-radius: 12px; background: var(--primary-soft); color: var(--primary);
  display: grid; place-items: center; }
.feature__title { font-size: 16.5px; font-weight: 700; color: var(--text-1); margin: 14px 0 8px; }
.feature__desc { font-size: 14.5px; color: var(--text-3); line-height: 1.7; }
.feature__list { margin-top: 14px; display: grid; gap: 8px; }
.feature__list li { display: flex; gap: 8px; align-items: flex-start; font-size: 13.5px; color: var(--text-3); min-width: 0; }
.feature__list li::before { content: ""; flex: none; width: 16px; height: 16px; margin-top: 2px;
  background: var(--primary); -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E") center/contain no-repeat;
          mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E") center/contain no-repeat; }
@media (max-width: 1024px) { .features { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 640px)  { .features { grid-template-columns: 1fr; } }
```

> 勾选点用 SVG mask 而非 emoji / 字符 ✓，符合红线第 9 条。

---

## D3. security-band（安全横带）

- 满宽 `bg-alt` 上下**无边带**（section 纵向 padding 可收窄）。
- 左标题 / 右文案（或**安全四点网格**）+ 大图标区。

```css
.security-band { background: var(--bg-alt); padding: 64px 0; border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light); }
.security-band__grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px; margin-top: 32px; }
@media (max-width: 900px) { .security-band__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
```

---

## D4. developers（开发者区）

左文右码：

- 代码块深色 `--bg-code`、`12.5px` mono + 头部 mac 三点 + 语言 Chip。
- 三步流程小卡。
- 代码示例支持 **curl / python / node 三 tab**（顶部胶囊切换）。

```css
.codeblock { background: var(--bg-code); border-radius: var(--radius-lg); overflow: hidden; border: 1px solid #1e293b; }
.codeblock__bar { display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 14px; background: #111827; }
.codeblock__lang { margin-left: auto; }
.codeblock pre { margin: 0; padding: 16px 18px; font: 12.5px/1.7 ui-monospace, Menlo, Consolas, monospace;
  color: #e2e8f0; overflow-x: auto; }

.tabs { display: inline-flex; gap: 4px; padding: 4px; background: var(--bg-alt); border: 1px solid var(--border-light); border-radius: 999px; }
.tabs__btn { height: 32px; padding: 0 14px; border-radius: 999px; font-size: 13px; font-weight: 600; color: var(--text-3); background: none; border: 0; cursor: pointer; }
.tabs__btn.is-active { background: #fff; color: var(--primary); box-shadow: var(--shadow-panel); }
```

---

## D5. pricing（定价）

卡片栅格 3 列，做**高低层次**（推荐卡用主蓝 / 白卡对比）：

- 含 `feature list ✓`、CTA 按钮、底部小字条款（`.price-note`）。

```css
.pricing { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; align-items: start; }
.plan--featured { border-color: var(--primary); box-shadow: var(--shadow-panel); transform: translateY(-4px); }
.plan--featured .plan__cta { background-image: var(--grad-cta); color: #fff; }
.price-note { font-size: 12px; color: var(--text-4); margin-top: 12px; }
@media (max-width: 900px) { .pricing { grid-template-columns: 1fr; } .plan--featured { transform: none; } }
```

---

## D6. partners（合作伙伴与客户，FAQ 之前）

### logo 墙

- **双排反向无限 marquee**：`210×68` 白底 chip、`12px` 间隙、hover 暂停、**灰度 → 彩色**。
- 两端 mask 渐隐（复用 D1 的 `.marquee`）。

```css
.logo-wall__chip { width: 210px; height: 68px; display: grid; place-items: center;
  background: #fff; border: 1px solid var(--border-light); border-radius: var(--radius-md);
  filter: grayscale(1); opacity: .75; transition: filter .25s ease, opacity .25s ease; }
.logo-wall__chip:hover { filter: grayscale(0); opacity: 1; }
```

### 客户案例卡

- 全幅封面：渐变 banner 交替色（A2 四色）+ 反白大 logo / 首字母块 + 右下大光斑装饰圆。
- hover 弹出 **kkidc 式深蓝灰（`#33425a`）白字面板**（从左 / 右交替滑入）。

```css
.case-card { position: relative; border-radius: var(--radius-lg); overflow: hidden; min-width: 0; }
.case-card__cover { position: relative; min-height: 220px; display: grid; place-items: center; color: #fff; }
.case-card__glow { position: absolute; right: -60px; bottom: -60px; width: 200px; height: 200px; border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,.45), transparent 65%); }
.case-card__panel { position: absolute; inset: auto 0 0 0; background: #33425a; color: #fff; padding: 20px;
  transform: translateY(100%); transition: transform .28s cubic-bezier(.32,.72,0,1); }
.case-card:hover .case-card__panel { transform: none; }
.case-card--from-left .case-card__panel  { }
.case-card--from-right .case-card__panel { }
```

---

## D7. faq

**左右分栏**：

- 左 `340px` **蓝紫渐变粘性卡**：`position: sticky; top: 110px`；含 eyebrow + 标题 + 说明 + 深色胶囊 CTA + `2h / 99.9%` 数据点。
- 右 **序号手风琴**：`01–06` 序号芯片、激活变实色蓝底白字、展开蓝投影、**答案缩进 `62px`**。

```css
.faq { display: grid; grid-template-columns: 340px 1fr; gap: 48px; align-items: start; }
.faq__sticky { position: sticky; top: 110px; padding: 28px; border-radius: var(--radius-lg); background: var(--grad-brand); color: #fff; }
.faq__answer { padding: 0 20px 18px 62px; color: var(--text-3); line-height: 1.75; }
.faq__item.is-open { border-color: var(--primary-border); box-shadow: 0 8px 26px rgba(37, 99, 235, .08); }
@media (max-width: 900px) { .faq { grid-template-columns: 1fr; gap: 24px; } .faq__sticky { position: static; } .faq__answer { padding-left: 20px; } }
```

---

## D8. cta-band

全宽**渐变蓝紫横带大卡**：标题 + 副文案 + 两颗按钮（白底实心 & 白描边 ghost）+ 底部装饰圆。

```css
.cta-band { border-radius: var(--radius-lg); background: var(--grad-brand); color: #fff;
  padding: 56px 48px; position: relative; overflow: hidden; }
.cta-band__glow { position: absolute; right: -80px; bottom: -120px; width: 320px; height: 320px; border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,.28), transparent 62%); }
.cta-band__actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 24px; }
.btn--white { background: #fff; color: var(--ink); }
.btn--ghost-light { background: transparent; border-color: rgba(255,255,255,.6); color: #fff; }
```

---

# E. 页脚（四层）

```text
① 白底区域：grid 2.2fr / 1fr / 1fr / 1fr
   品牌栏（logo + 简介 + 联系地址 / 邮箱 / 电话蓝点行）
   + 产品 / 开发者 / 支持 三列
   列标题 12px uppercase 字距 .1em；链接 13.5px text-3，hover 蓝 + 右移 2px
② 1px 细线
③ 主体双卡：.footer-entity-grid —— 🇨🇳 中文主体 | 🇭🇰 国际主体
   底部行：STRATEGIC PARTNERSHIP ●●●（三色呼吸点） ↔ 战略标语
④ Powered by 行：绿点脉冲 ↔ 主体英文
   浅灰通栏 legal bar：© 版权 · 服务条款 · 隐私政策 · ICP（可点链工信部）| safe-area
```

```css
.footer { background: var(--bg); border-top: 1px solid var(--border-light); }
.footer__grid { display: grid; grid-template-columns: 2.2fr 1fr 1fr 1fr; gap: 40px; padding: 64px 0; }
.footer__col-title { font-size: 12px; text-transform: uppercase; letter-spacing: .1em; color: var(--text-4); font-weight: 700; }
.footer__link { display: inline-flex; align-items: center; font-size: 13.5px; color: var(--text-3); text-decoration: none;
  transition: color .18s ease, transform .18s ease; }
.footer__link:hover { color: var(--primary); transform: translateX(2px); }
.footer__contact-row { display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--text-3); }
.footer__contact-row::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--primary); flex: none; }

.footer__entity-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;
  border-top: 1px solid var(--border-light); padding-top: 24px; }
.footer__entity-card { border: 1px solid var(--border); border-radius: var(--radius-md); padding: 16px 20px; background: var(--bg); min-width: 0; }
.footer__entity-foot { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-top: 12px; font-size: 12px; color: var(--text-4); }
.footer__dots span { width: 8px; height: 8px; border-radius: 50%; display: inline-block; box-shadow: 0 0 0 3px rgba(37,99,235,.10); }
.footer__dots span:nth-child(1) { background: var(--primary); }
.footer__dots span:nth-child(2) { background: #7c3aed; }
.footer__dots span:nth-child(3) { background: #0891b2; }

.footer__powered { display: flex; align-items: center; gap: 10px; font-size: 12.5px; color: var(--text-3); }
.footer__legal { background: var(--bg-alt); color: var(--text-3); font-size: 12px; padding: 16px 0 calc(16px + env(safe-area-inset-bottom)); }
.footer__legal a { color: var(--text-3); text-decoration: none; }
.footer__legal a:hover { color: var(--primary); }

@media (max-width: 900px) {
  .footer__grid { grid-template-columns: 1fr; gap: 28px; padding: 48px 0; }
  .footer__entity-grid { grid-template-columns: 1fr; }
  .footer__legal { text-align: center; line-height: 1.9; }
}
```

## 数据来源（关键）

页脚数据全部来自 `/api/v1/site-config`：

| 字段 | 用途 |
|---|---|
| `footer_entity_*` | 主体双卡（中文主体 / 国际主体） |
| `footer_slogan` | 战略标语 |
| `footer_powered_by` | Powered by 主体英文 |
| `footer_address` / `footer_email` / `footer_phone` | 品牌栏联系行 |
| `site_icp` | legal bar 的 ICP 备案号 |

**空值时对应元素自动 `hidden`**——不要渲染空壳或占位符。

> 白标（white-label）场景下，品牌名、主体、联系方式、ICP 全部走该接口，禁止在组件内硬编码。
