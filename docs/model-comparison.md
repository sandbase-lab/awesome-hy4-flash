# Hy4 Flash vs DeepSeek V4.1 Flash 1017, Claude Opus 5.5 and Hy4

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Posts on X with their own prompts, costs and times. Useful context, not verified by us.

Hy4 Flash was announced on November 16, 2026. Its measured side is empty for now, and the creator side is small. Read the numbers below with that in mind.

## What we measured: Lab Evals boards and Pelican Test

**There is no Hy4 Flash row on the Lab Evals boards or the Pelican Test leaderboard yet.** The source data for this list has no Evals or Pelican score for the model, so this page quotes none. Until one exists, nothing here places Hy4 Flash against the frontier or against DeepSeek V4.1 Flash 1017.

To see where the rivals stand, open the [Evals boards][evals] and the [Pelican Test][pelican] directly. Those pages carry the dated snapshots, and this page will link a Hy4 Flash row as soon as one is added in a normal PR.

## What creators reported

Posts on X that show Hy4 Flash running a prompt, with what the creator said about it. The numbers are the creator's own: different tools (WorkBuddy, OpenRouter, direct API), different reasoning settings and often one run. Click through to see both results.

| Creator | Task | Hy4 Flash | Rival | Creator's words |
|---|---|---|---|---|
| [@ItsmeAjayKV][dragonfly] | Mechanical flying dragonfly, one-shot, no harness, no tool calls | Same prompt | DeepSeek V4.1 Flash 1017 (high) | DeepSeek's result is "more mechanical"; Hy4 Flash "does the job, but it's more basic"; the two used "way different token count for same task" |
| [@DesignArena][keyboard] | Mechanical keyboard that disassembles and reassembles by layer, 3D | $0.070 per million input tokens, $0.281 per million output, $0.003 per million cached input | Hy4 (the larger model) | "Hy4 includes more detail and realistic l…" (cut off in the source) |
| [@CodeByPoonam][peacock] | Peacock dance test | Free, via WorkBuddy | Claude Opus 5.5 | "Same prompt. Same settings. One shot." The post gives no verdict |
| [@Andy_whhh][pelican-post] | Pelican riding a bicycle, 2D SVG animation in one HTML file | Free "for now" | GPT-6.1 Sol (written "GP6.1 sol" in the post) | "HY4 flash 和豆包一个级别" ("Hy4 Flash is in the same tier as Doubao"); cost-effective, given that it is free |
| [@hasantoxr][platformer] | Browser platformer from a paper sketch and a pixel-art screenshot | Open-weight and free in WorkBuddy; "it can see images and use your computer" | None | "it genuinely surprised me" |
| [@loktar00][bee] | 3D bee, early local test | Early access, run locally | None | "for 224b with 12b active parameters I like it" |

What these posts say, and what they don't:

- **Price is the consistent point.** The DesignArena list price matches the SandBase model page ([model page][model]). Several creators report Hy4 Flash as free in WorkBuddy; that is free access in one tool, not a per-token price.
- **Quality is split.** One creator preferred DeepSeek V4.1 Flash 1017 on the dragonfly. Another placed Hy4 Flash in Doubao's tier. DesignArena's comparison notes that the larger Hy4 adds detail.
- **Specs are creator-reported.** The 224B total and 12B active parameter figures come from two creators (@loktar00 and @Andy_whhh, the latter also gives a 1M context and over 150 tokens per second). The model's listed context window is in [`inspect`](https://www.sandbase.ai/model/tencent/hy4-flash).
- **Sample size.** Six prompt-shared posts, most of them one run each. The creator list will grow as the collection does.

## Rerun before you trust a comparison

Results move a lot with the setup. Run the prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals]: Artificial Analysis data, with dated snapshots. Search for "Hy4" to see whether a row has appeared.
- [Lab Pelican Test][pelican]: same prompt on every model, scored the same way, with the drawings on screen.
- [All AI video collections on SandBase Lab][collections]: the same list for other models.

---

Creator data: their posts, linked; not independently verified. Translations from Chinese are ours.

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
