# Hy4 Flash 提示词写法：如何为视频提示 Hy4 Flash

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

Hy4 Flash 不直接输出视频。它写代码，通常是用 Three.js、SVG、Canvas 或 CSS 动画的 HTML 页面，作者再把页面播放过程录下来。下面的写法来自本合集中随视频公开了提示词的六条作者帖子，以及该模型公开列出的能力中这些帖子用到的部分。每条都链接到它的来源帖子。合集还年轻，这份指南会随着更多提示词公开而增长。

## 1. 只写一个具体的物体，以及它怎么动

公开提示词的作者都选了一个具体物体，并描述它的动作：

- "a mechanical keyboard that disassembles and reassembles by layer"（一把机械键盘，按层拆开、再组装回去）（[@DesignArena][keyboard]，同一个 3D 提示词同时用在 Hy4 Flash 和 Hy4 上）。
- "a mechanical flying dragonfly"（一只会飞的机械蜻蜓）（[@ItsmeAjayKV][dragonfly]，一次生成，没有 harness，也没有工具调用）。

物体具体，动作也写进需求里。这样模型有东西可以搭建，录制时也能拍到。

## 2. 写清文件，也写清绘制方式

本合集里最清楚的需求，说明了要写哪个文件，以及用什么方式画：

- "创建一个 HTML，内容是 SVG 绘制一个鹈鹕骑自行车的 2D 动画。"（[@Andy_whhh][pelican]）

一个 HTML 文件加一个指定的渲染方式（这里是 SVG），让输出既小又好录制。要点名渲染方式，而不只写"3D"或"动画"：同一个主体用 Three.js 和用 SVG 做出来，效果差别很大。

## 3. 有图就从图开始

Hy4 Flash 接受图片输入。有一位作者用它把手绘变成了游戏：他拍了一张手画的平台跳跃关卡，又截了一张喜欢的像素风游戏截图，然后只写了一条提示词：

- "Turn this paper sketch into a browser platformer. Match th…"（"把这张纸上的草图做成一个浏览器平台跳跃游戏。匹配…"）（[@hasantoxr][platformer]；帖子中的提示词在此处被截断，完整内容请打开原帖。）

如果你的想法已经在纸上或屏幕上，就把它附上，并说明要保留什么。不要凭记忆描述。

## 4. 预计输出 token 会有差异，并为此留预算

同一个任务，两个模型的输出量可能差别很大。一位把 Hy4 Flash 与 DeepSeek V4.1 Flash 1017 做对比的作者说，两者对同一任务用了"way different token count"（差异很大的 token 数）（[@ItsmeAjayKV][dragonfly]）。SandBase 上 Hy4 Flash 的 `max_tokens` 上限是 64,000，所以长页面的预算要在这个上限之内。如果响应被截断，就在上限之内调高额度、简化需求，或者把场景拆开。

## 5. 对比时保持设置完全一致

公开对比的作者都用同一个提示词、同一套设置，并且会说明。CodeByPoonam 的孔雀舞测试写的是："Same prompt. Same settings. One shot."（同一个提示词，同样的设置，一次生成。）（[@CodeByPoonam][peacock]）。工具、推理强度或尝试次数不同，结果就会不同。你发布对比时要把这些写在旁边，或者自己到 [Lab 文本竞技场][arena] 上跑一遍。

## 6. 按你需要的细节选择档位

Hy4 Flash 是性价比更高的一档。DesignArena 用同一个 3D 提示词分别跑了 Hy4 Flash 和更大的 Hy4，并报告"Hy4 includes more detail"（Hy4 细节更丰富）（[@DesignArena][keyboard]）。量大时先用 Flash；场景需要更高的还原度时，用同一个提示词跑更大的模型，然后并排比较两份输出。

## 可以直接用的提示词

```text
把 [主体] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

画面：[风格，例如 SVG 扁平 / Three.js low-poly / 像素风]，[氛围、光照、配色]。
运动：[什么在动、怎么动]。加载后自动播放 [10] 秒的循环，然后重复。
交互：[拖拽 = …，点击 = …，按键 = …]。
规则：[必须遵守的数字：部件数、生命、齿轮比、时序]。

技术：
- 只用内联代码，不要外部图片、字体或音频。
- Three.js 用 CDN import map 以 ES module 引入，或只用 SVG/CSS，二者不要混用。
- 铺满视口，不出现滚动条。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场][arena] 里，把这段同时跑在 Hy4 Flash 和其他模型上对比；用 API 的方式见[教程](tutorial.md)。

## 参数设置

- **输出预算。** 这个模型的 `max_tokens` 上限是 64,000，README 里的 curl 示例直接取该上限。
- **模型档位。** Hy4 Flash 是 Hy4 系列中性价比更高的一档。想在同一提示词下获得更多细节，就和更大的 Hy4 对比（见第 6 条）。

---

引文均为短摘录并注明作者，完整帖子请点链接。中文原文的翻译为我们所做。

[keyboard]: https://x.com/DesignArena/status/2122429321151435237
[dragonfly]: https://x.com/ItsmeAjayKV/status/2122415420665921735
[pelican]: https://x.com/Andy_whhh/status/2122350545977618841
[platformer]: https://x.com/hasantoxr/status/2123085293414916457
[peacock]: https://x.com/CodeByPoonam/status/2123028120483901925
[arena]: https://www.sandbase.ai/arena/text?models=tencent%2Fhy4-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
