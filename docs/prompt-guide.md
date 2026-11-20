# Hy4 Flash prompt guide: how to prompt Hy4 Flash for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Hy4 Flash doesn't output video. It writes code, usually an HTML page with Three.js, SVG, Canvas or CSS animation, and the creator records that page playing. The patterns below come from the six creator posts in this collection that shared their prompt, plus the parts of the model's listed capabilities that those posts used. Each pattern links to the post it came from. The collection is young, so this guide is short and will grow as more prompts are shared.

## 1. Name one concrete object and how it moves

Creators who shared a prompt picked a single object and described what it does:

- "a mechanical keyboard that disassembles and reassembles by layer" ([@DesignArena][keyboard], a 3D prompt used on both Hy4 Flash and Hy4).
- "a mechanical flying dragonfly" ([@ItsmeAjayKV][dragonfly], run one-shot, with no harness and no tool calls).

The object is concrete, and the motion is part of the brief. That gives the model something it can build and a recording can catch.

## 2. Name the file and the drawing method

The clearest brief in the collection says what file to write and how to draw the picture:

- "创建一个 HTML，内容是 SVG 绘制一个鹈鹕骑自行车的 2D 动画。" ("Create an HTML file whose content is a 2D SVG animation of a pelican riding a bicycle," [@Andy_whhh][pelican], translated.)

One HTML file plus one named renderer (SVG here) keeps the output small and easy to record. Name the renderer, not just "3D" or "animation". The same subject can come out very differently in Three.js and in SVG.

## 3. Start from an image when you have one

Hy4 Flash accepts image input, and one creator used it to turn a drawing into a game. They photographed a hand-drawn platformer level, screenshotted a pixel-art game they liked, and wrote one prompt:

- "Turn this paper sketch into a browser platformer. Match th…" ([@hasantoxr][platformer], the prompt continues past this point; the post text is cut off in the source, so read the full post for the rest.)

If your idea already exists on paper or on screen, attach it and describe what to keep. Don't describe it from memory.

## 4. Expect the token count to vary, and budget for it

Two models given the same task can use very different amounts of output. One creator comparing Hy4 Flash with DeepSeek V4.1 Flash 1017 said the two used "way different token count for same task" ([@ItsmeAjayKV][dragonfly]). Hy4 Flash's `max_tokens` is capped at 64,000 on SandBase, so a long page needs a budget that fits under that cap. If the response is cut off, raise the limit within the cap, simplify the brief, or split the scene.

## 5. Keep the settings identical when you compare

The creator posts that compare models share one prompt and one setting, and say so. CodeByPoonam's peacock-dance comparison reads: "Same prompt. Same settings. One shot." ([@CodeByPoonam][peacock]). Differences in tool, reasoning setting or number of attempts change the result, so write those down next to any comparison you publish, or run it yourself on the [Lab text arena][arena].

## 6. Pick the tier that matches the detail you need

Hy4 Flash is the cost-efficient tier. DesignArena ran the same 3D prompt through Hy4 Flash and the larger Hy4, and reports that "Hy4 includes more detail" ([@DesignArena][keyboard]). Start with Flash for volume. When the scene needs more fidelity, run the same prompt on the larger model and compare the two outputs side by side.

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. SVG flat / Three.js low-poly / pixel-art], [mood, lighting, palette].
Motion: [what moves and how]. Autoplay a [10]-second loop on load, then repeat.
Interaction: [drag = …, click = …, keys = …].
Rules: [the numbers it must respect: parts, lives, gear ratios, timing].

Technical:
- Use only inline code. No external images, fonts or audio.
- Use Three.js as an ES module from a CDN import map, or plain SVG/CSS, not both.
- Fill the viewport, no scrolling.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it on the [Lab text arena][arena] to run it on Hy4 Flash and other models side by side, or with the API in the [tutorial](tutorial.md).

## Settings

- **Output budget.** `max_tokens` is capped at 64,000 for this model. The README's curl example asks for that maximum.
- **Model tier.** Hy4 Flash is the cost-efficient tier of the Hy4 family. For more detail on the same prompt, compare with the larger Hy4 (see pattern 6).

---

Quotes are short excerpts credited to their authors; follow the links for full posts. Translations from Chinese are ours.

[keyboard]: https://x.com/DesignArena/status/2122429321151435237
[dragonfly]: https://x.com/ItsmeAjayKV/status/2122415420665921735
[pelican]: https://x.com/Andy_whhh/status/2122350545977618841
[platformer]: https://x.com/hasantoxr/status/2123085293414916457
[peacock]: https://x.com/CodeByPoonam/status/2123028120483901925
[arena]: https://www.sandbase.ai/arena/text?models=tencent%2Fhy4-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
