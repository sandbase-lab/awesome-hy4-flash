# Hy4 Flash 提示词

[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

共 12 条 Hy4 Flash 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 Hy4 Flash 一键 **复刻**。第一次写 Hy4 Flash 提示词？先看 [提示词写法](prompt-guide.md)。

每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。

- [3D 场景](#3d-scene) (3)
- [动效](#motion-graphics) (1)
- [游戏](#game) (1)
- [测试对比](#comparison) (7)

<a id="3d-scene"></a>

## 3D 场景

### 使用Hy4-Flash模型生成的蜜蜂视频

[@loktar00](https://x.com/loktar00/status/2122411723936485494) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2122411723936485494/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2122411723936485494?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
HEY!! This is an exciting model coming locally! Hy4-Flash

I got early access so got to run a few tests and for 224b with 12b active parameters I like it!

Here's my bee prompt with it. Will post a few more throughout today, this is actually exciting!
```

### 带动态灯光的交互式3D音乐室

[@GesoraMeshack](https://x.com/GesoraMeshack/status/2123455572465139746) · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2123455572465139746/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2123455572465139746?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
I gave Hy4 Flash and DeepSeek-V4.1-Flash the same prompt in WorkBuddy: build an interactive 3D music room.

Hy4 Flash finished in 31 minutes. DeepSeek took 37.

Here’s the Hy4 Flash version, with changing lights, rain outside, and a clickable laptop.
```

### Three.js中模拟摩卡壶煮咖啡

[@VRAMCalculator](https://x.com/VRAMCalculator/status/2123524789184713006) · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2123524789184713006/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2123524789184713006?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
We made Hy4 Flash brew coffee.

One prompt each, no fixes, no second tries:
1. Build a moka pot in Blender, take it apart, put it back, cut it open.
2. Animate how it brews in three.js.

Same laptop, same prompts for every model we test next. Scores below.
```

<a id="motion-graphics"></a>

## 动效

### 鹈鹕骑自行车的SVG动画生成效果

[@Andy_whhh](https://x.com/Andy_whhh/status/2122350545977618841) · 0:11 · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2122350545977618841/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2122350545977618841?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
刚刚再次测评了一下 腾讯混元今天的新模型HY4 flash！

我拿 GP6.1 sol 跟他 做了1版

提示词都一下的：创建一个 HTML，内容是 SVG 绘制一个鹈鹕骑自行车的 2D 动画。

画面你们看了也知道 😂

HY4 flash 和豆包一个级别

好在，目前是免费的

它的核心参数如下

总参数：2240 亿
激活参数：120 亿
上下文：100 万 Token
推理速度：超过 150 Token/s
支持多模态输入

综合来说，在低成本这方面来说，性价比还是蛮高的
```

<a id="game"></a>

## 游戏

### 根据手绘草图生成的网页平台跳跃游戏

[@hasantoxr](https://x.com/hasantoxr/status/2123085293414916457) · 0:56 · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2123085293414916457/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2123085293414916457?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
DROP EVERYTHING

Hy4 flash is now open-weight and free to use in WorkBuddy right now and it can see images and use your computer.

I tested it tonight and it genuinely surprised me.

Here's the test I ran:

I drew a messy platformer level on paper. Took a photo. Grabbed a screenshot of a pixel art game I love.

Then I gave it one prompt:

"Turn this paper sketch into a browser platformer. Match the art style of this screenshot. Add a title screen, 3 levels that get harder, coins, enemies, a death screen and a restart button."

It looked at my sketch. Understood where the platforms, gaps and enemies were. Pulled the color palette and vibe from the screenshot.

Then it built the whole thing.

Playable. In the browser. Win and lose states working. Levels actually getting harder.

From a photo of a napkin drawing.

What stood out to me:

It's fast. Really fast.
The output quality is way above what I expected from a flash model.
It didn't burn through a ton of steps getting there.

A year ago this needed a designer, a dev and a weekend.

Now it needs a pen and one prompt.

The best part: Hy4 flash is free to use in WorkBuddy right now.

Download WorkBuddy, open the model picker, select Hy4 flash.

Try it before everyone else does.

Link:
```

<a id="comparison"></a>

## 测试对比

### Hy4-Flash与DeepSeek-v4.1生成的机械蜻蜓对比

[@ItsmeAjayKV](https://x.com/ItsmeAjayKV/status/2122415420665921735) · 0:34 · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2122415420665921735/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2122415420665921735?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
Hy4-Flash vs DeepSeek-v4.1-Flash-1017 !

Left: deepseek-v4.1-flash-1017 (high)
Right: hy4-flash (high)

Both one-shot, no harness, no tool calls, same prompt to create a mechanical flying dragonfly !

Two flash models, but way different token count for same task.

Looking at the result itself, deepseek-v4.1-flash one is better, it's more mechanical. Hy4-flash does the job, but it's more basic and fall short on the expectation.

When it comes to token usage: 

Deepseek-v4.1-flash: 
think 68,304 | answer 14,708 |  out 83,012

Hy4-flash: 
think 15,456 | answer 5,205 | out 20,661
```

### Hy4与Hy4-Flash生成的机械键盘拆解对比

[@DesignArena](https://x.com/DesignArena/status/2122429321151435237) · 0:12 · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2122429321151435237/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2122429321151435237?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
Hy4 Flash by @TencentHunyuan is now available on DesignArena!

Hy4 Flash is Tencent’s new low-cost model for everyday productivity, at $0.070 per million input tokens, $0.281 per million output tokens, and $0.003 per million cached input tokens.

We gave Hy4 Flash and Hy4 the same 3D prompt: a mechanical keyboard that disassembles and reassembles by layer.

Hy4 includes more detail and realistic lighting, with its keyboard casting shadows that reflect its disassembly state.

Hy4 Flash is 8x cheaper and 2x faster. And surprisingly, Hy4 Flash built the mechanical keyboard people expect, with the standard QWERTY layout, whereas Hy4 opted instead for an ortholinear grid of same-size keys.

Congrats to the @TencentHunyuan team on the launch!
```

### 多模型孔雀舞动画生成效果对比

[@CodeByPoonam](https://x.com/CodeByPoonam/status/2123028120483901925) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2123028120483901925/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2123028120483901925?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
$20 CLAUDE OPUS 5.5 VS FREE HY4 FLASH ON MY PEACOCK DANCE TEST

Same prompt. Same settings. One shot.

· Tencent Hy4 flash (WorkBuddy):  free
· Gemini 4 Hydrogen: $1.50/mo
· GPT-6 Astra: $20/mo
· Claude Opus 5.5: $20/mo

Pick your winner.. Full Breakdown with Prompt👇
```

### 编写地铁跑酷克隆版代码的模型对比

[@HeyToha](https://x.com/HeyToha/status/2123876649410445728) · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2123876649410445728/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2123876649410445728?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
I put Tencent's Hy4 Flash and DeepSeek-V4.1-Flash head-to-head in a real coding challenge.

Both got the exact same prompt: build a playable Subway Surfers clone from scratch.

The results from my tests were quite surprising:

→ Hy4 Flash: 7 minutes 38 seconds

→ DeepSeek-V4.1-Flash: 1 hour 30 minutes

DeepSeek also consumed HALF of my account credits.

I'm genuinely impressed by Hy4 Flash's speed.

Here's the full comparison: 🧵👇

Here's Hy4 Flash building the game. Watch how fast it gets done: (COMPLETED IN JUST 7 MINUTES) ↓↓
```

### 雨夜霓虹加油站3D场景生成对比评测

[@0xBakeer](https://x.com/0xBakeer/status/2124571168417923471) · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2124571168417923471/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2124571168417923471?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
I gave three quants the same prompt: build a rainy neon gas station at night as one animated 3D page.

Hy4-flash at 3.56 and 3.08 bits per weight, and Qwen3.8-Flash-Next at 3.05. Each one ran in opencode against my engine with nothing around it, reasoning at the maximum, on the DGX Spark.

But the fastest one finished last 👀

Flash-Next writes 67 tok/s and the Hy4 packs write 42 and 43. It still needed 32 min 43 s. The two Hy4 packs finished in 20 min 28 s and 13 min 25 s.

Its run wrote 123k tokens. The Hy4 runs wrote 48k and 31k.
```

### Hy4 Flash两种量化版本的对比演示

[@EamonMcKiernan5](https://x.com/EamonMcKiernan5/status/2124900065546244489) · [观看](https://www.sandbase.ai/lab/media/x/hy4-flash/2124900065546244489/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2124900065546244489?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
Only now realising I never showed off my Hy4 Flash runs in Project Maya😅

@PeasantSmith Hy4-Flash-Maya-M (left) vs Hy4 Flash API (right)

This is an amazing quant, so much quality kept at IQ3-XSS. I don't have many Maya-M demos built so far, but the few I do have, it's genuinley hard to tell which is which.

Full prompt, builds, and session stats on my website linked below!
```

### 两款模型生成的太阳系网页对比

[@aapakari](https://x.com/aapakari/status/2125314175467491405) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125314175467491405/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/hy4-flash/2125314175467491405?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash&utm_content=prompt-index)

```text
One prompt, two models: "a small solar system with moons, an asteroid belt and a comet", as one web page.

Gemini 4 Hydrogen (high): 1 min 17 s, $0.15
Hy4 Flash (default setting): 53 s, $0.004

Hydrogen cost 35x the price of Hy4 Flash for the same prompt.

Which one would you ship?
```
