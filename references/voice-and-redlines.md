# 文案语气 · F 九条红线 · G 使用模板 · 交付自检

## 一、语气与文案

- 中文简体，克制专业。用词示例：「统一接入」「按量计费」「分钟级完成接入」。
- 英文点缀用**大写小标签**（`MODELS` / `DEVELOPERS` / `STRATEGIC PARTNERSHIP`）：
  `10–11px / 600 / letter-spacing .1–.12em / uppercase / --text-4`。
- 状态文案带绿点（如 `● Powered by …`）。
- **不使用感叹号堆叠**；用事实与数字说话。
- 数字统一 `font-variant-numeric: tabular-nums`。

### 好 / 坏对照

| 场景 | ✅ 推荐 | ❌ 避免 |
|---|---|---|
| 接入速度 | 分钟级完成接入 | 超快！！秒接入！！！ |
| 计费 | 按量计费，用多少付多少 | 全网最低价，错过再等一年 |
| 能力 | 统一接入主流模型 | 颠覆行业，史无前例 |
| 状态 | ● Powered by XXX | 系统超级稳定！ |

### 图标

- 统一 **SVG 线性**：`stroke-width 1.5–2`、`round` cap/join、`fill: none`。
- 品牌图可用 [lobehub icons](https://icons.lobehub.com)（id 全小写折叠拼接）。
- **禁止用 emoji 充当功能图标**（页脚 🇨🇳 / 🇭🇰 地域标识除外）。

---

## 二、F. 九条红线（负面提示词）

1. ❌ **禁大面积低对比灰字压灰底**——文字色彩不得浅于 `--text-3`。
2. ❌ **禁黑色重阴影**——所有阴影都是「大距离 + 低透明度 + 蓝主色系」。
3. ❌ **禁 `transition: all`**——只过渡 `opacity / transform / border-color / color`。
4. ❌ **禁直角突变**——按钮 `999px` 胶囊，卡片 `≥14px`。
5. ❌ **含可换行文本的 flex 子项必须 `min-width: 0`**，否则长英文 id 撑爆卡片右侧。
6. ❌ **悬浮元素（nav / notice / mega / 抽屉）必须 `blur + border + shadow` 三件套**，禁无层次贴面出现。
7. ❌ **移动端 fixed 底部元素必须加 `env(safe-area-inset-bottom)`**。
8. ❌ **`content-visibility: auto` 只用于首屏外区块**，且必须配 `contain-intrinsic-size: 720px`。
9. ✅ **所有颜色仅来自变量表**；需要新增色必须先在 A1 注册。

---

## 三、G. 一句话使用模板

> 「基于上述设计语言，为 MiniRelax 落地页新增 XX 区块/页面：遵循 A 色彩变量 + B 顶栏胶囊 + C 打字机 hero +
> D.x 对应区块样式 + E 页脚四层结构；动效与响应式遵守 A/F，红线 F 全部满足；白标文案走 `/api/v1/site-config`。」

按需把 `XX` 替换为具体区块，例如：

- 「新增 **D5 定价区块**：3 列卡片栅格 + 推荐卡主蓝高亮 + 底部 `price-note` 条款。」
- 「新增 **D6 合作伙伴页**：双排反向 logo 墙 + 案例卡 hover 弹出 `#33425a` 面板。」
- 「新增 **500 错误页**：使用 `--grad-500`（橙→红→粉）渐变，配返回首页主 CTA。」

---

## 四、交付自检清单

**Token**
- [ ] 颜色全部走变量，无散落硬编码色值，无未注册新色
- [ ] 圆角只用 `999 / 16 / 12 / 10 / 8` 家族
- [ ] 阴影全部蓝主色系 / 中性蓝灰，无黑色重阴影

**组件与区块**
- [ ] 顶栏为悬浮胶囊（不占通栏）+ blur + border + 双阴影，滚动 `>8px` 吸顶
- [ ] 导航槽为浅灰胶囊，激活态主蓝 + 白底浮起；翻字 + 短下划线兜底
- [ ] Hero 打字机 + 渐变字弹入 + 2×2 按钮阵 + hero-stats 四格 + 深色双 pane 演示窗
- [ ] 内容区按 D.x 实现（信任条 / features / security / developers / pricing / partners / faq / cta-band）
- [ ] FAQ 左 `340px` 粘性渐变卡 + 右侧 `01–06` 序号手风琴，答案缩进 `62px`
- [ ] 页脚四层齐全；空字段按 site-config 规则 `hidden`

**红线 F**
- [ ] 无低对比灰字压灰底（正文 ≥ `--text-3`）
- [ ] 无黑色阴影；无 `transition: all`
- [ ] 按钮 999px、卡片 ≥14px，无直角突变
- [ ] 含长文本的 flex 子项都有 `min-width: 0`
- [ ] 悬浮元素 blur + border + shadow 三件套齐全
- [ ] 移动端所有 fixed 底部元素处理了安全区
- [ ] `content-visibility: auto` 仅首屏外且配 `contain-intrinsic-size: 720px`
- [ ] 颜色全部来自变量表

**动效 / 响应式 / 可访问性**
- [ ] 入场为编排序列（`badge → H1 → 渐变行 → CTA → stats → demo`）
- [ ] `prefers-reduced-motion` 降级覆盖打字机 / 跑马灯 / 呼吸点 / 翻字
- [ ] 三档断点行为正确；`≤768` 汉堡单列、Hero 顶部 `108px`
- [ ] 触摸目标 ≥ `44×44px`；可交互元素有可见 `focus-visible`
- [ ] 正文对比度 ≥ `4.5:1`

**文案**
- [ ] 白标信息全部来自 `/api/v1/site-config`，无硬编码品牌信息
- [ ] 无感叹号堆叠；英文标签为大写小字距风格
- [ ] 图标为 SVG 线性，无 emoji 充当功能图标
