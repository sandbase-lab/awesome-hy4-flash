# Hy4 Flash 对比 DeepSeek V4.1 Flash 1017、Claude Opus 5.5 和 Hy4

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 用同一份固定提示词跑每个模型并给结果打分。样本不大，但所有人的条件一致。
2. **创作者报告的。** 发在 X 上的帖子，附他们自己的花费和耗时。有参考价值，但我们没有验证。

Hy4 Flash 于 2026 年 11 月 16 日发布。目前实测一侧是空的，创作者一侧也还很少。读下面的数字时请记住这一点。

## 我们测到的：Lab Evals 榜单与 Pelican Test

**Hy4 Flash 目前在 Lab Evals 榜单和 Pelican Test 排行榜上都没有对应的行。** 本列表的源数据里没有该模型的 Evals 或 Pelican 分数，所以本页不引用任何实测数字。在有之前，这里没有任何内容能把它和前沿模型或 DeepSeek V4.1 Flash 1017 放在一起比较。

要查看对手的位置，请直接打开 [Evals 榜单][evals] 和 [Pelican Test][pelican]。这些页面带有带日期的快照；Hy4 Flash 的数据一旦加入，本页会通过正常的 PR 链接过去。

## 创作者报告的

在 X 上展示 Hy4 Flash 运行提示词的帖子，附作者的说法。数字是作者自己的：工具不同（WorkBuddy、OpenRouter、直接调用 API），推理设置不同，往往只跑一次。点进链接可以两边一起看。

| 创作者 | 任务 | Hy4 Flash | 对手 | 创作者原话 |
|---|---|---|---|---|
| [@ItsmeAjayKV][dragonfly] | 机械飞行蜻蜓，一次生成，无 harness，无工具调用 | 同一提示词 | DeepSeek V4.1 Flash 1017（high） | DeepSeek 的结果"更有机械感"；Hy4 Flash "does the job, but it's more basic"（能完成，但更基础）；两者对同一任务的 token 数"差异很大" |
| [@DesignArena][keyboard] | 按层拆解、再组装的机械键盘，3D | 每百万输入 token $0.070，每百万输出 token $0.281，每百万缓存输入 token $0.003 | Hy4（更大的模型） | "Hy4 includes more detail and realistic l…"（原文截断）（"Hy4 细节更多，光影更真实……"） |
| [@CodeByPoonam][peacock] | 孔雀舞测试 | 免费，通过 WorkBuddy | Claude Opus 5.5 | "Same prompt. Same settings. One shot."（同一提示词，同样设置，一次生成）。帖子没有给出结论 |
| [@Andy_whhh][pelican-post] | 骑自行车的鹈鹕，单个 HTML 文件内的 2D SVG 动画 | 免费"目前" | GPT-6.1 Sol（帖子中写作 "GP6.1 sol"） | "HY4 flash 和豆包一个级别"；考虑到免费，性价比不错 |
| [@hasantoxr][platformer] | 由纸上草图和像素风截图生成浏览器平台跳跃游戏 | 开放权重，WorkBuddy 中免费；"它能看图，也能操作电脑" | 无 | "它真的让我惊喜" |
| [@loktar00][bee] | 3D 蜜蜂，早期本地测试 | 抢先体验，本地运行 | 无 | "for 224b with 12b active parameters I like it"（224B 参数、激活 12B，我很喜欢） |

这些帖子说明什么，又不能说明什么：

- **价格是最一致的一点。** DesignArena 给出的标价与 SandBase 模型页一致（[模型页][model]）。好几位创作者说在 WorkBuddy 里免费使用 Hy4 Flash，那是某个工具里的免费使用，不是按 token 的价格。
- **质量意见分裂。** 一位作者在蜻蜓测试中更喜欢 DeepSeek V4.1 Flash 1017；另一位把 Hy4 Flash 归为豆包一个级别。DesignArena 的对比则指出，更大的 Hy4 细节更多。
- **规格是作者报告的。** 224B 总参数和 12B 激活参数来自两位作者（@loktar00 与 @Andy_whhh，后者还给出 100 万上下文、推理速度超过 150 token/s）。模型公开列出的上下文窗口见 [`inspect`](https://www.sandbase.ai/model/tencent/hy4-flash)。
- **样本量。** 六条公开提示词的帖子，大多是一次运行。随着合集增长，创作者列表也会增长。

## 重跑一次再相信对比

设置一变结果就变。自己跑一遍：把提示词粘到 [Lab 文本竞技场][arena]，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单][evals]：Artificial Analysis 数据，带日期快照。搜索 "Hy4" 可以看到是否已有对应行。
- [Lab Pelican Test][pelican]：同一提示词、同一评分方式，画作直接展示。
- [SandBase Lab 上的全部 AI 视频合集][collections]：其他模型的同类列表。

---

创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

[evals]: https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[pelican]: https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[arena]: https://www.sandbase.ai/arena/text?models=tencent%2Fhy4-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[model]: https://www.sandbase.ai/model/tencent/hy4-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[dragonfly]: https://x.com/ItsmeAjayKV/status/2122415420665921735
[keyboard]: https://x.com/DesignArena/status/2122429321151435237
[peacock]: https://x.com/CodeByPoonam/status/2123028120483901925
[pelican-post]: https://x.com/Andy_whhh/status/2122350545977618841
[platformer]: https://x.com/hasantoxr/status/2123085293414916457
[bee]: https://x.com/loktar00/status/2122411723936485494
