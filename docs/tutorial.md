# Hy4 Flash tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. Hy4 Flash writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and Hy4 Flash selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to Hy4 Flash (for example `deepseek/deepseek-v4.1-flash` or the larger Hy4) and run once. Every model gets the same words, and each result shows its cost and time. The creator comparisons on the [comparison page](model-comparison.md) often ran a single prompt once, so check a claim on your own task before you rely on it.

## 3. Or call the API

Hy4 Flash is `tencent/hy4-flash` on SandBase, OpenAI-compatible.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "tencent/hy4-flash",
  max_tokens: 64000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > hy4-flash.html
jq '.usage' response.json
```

- `max_tokens: 64000`: this is the maximum in the model's input schema from `sandbase inspect tencent/hy4-flash`, so the example uses that cap. If a long page is cut off, simplify the brief and split the scene (see [prompt guide, pattern 4](prompt-guide.md#4-expect-the-token-count-to-vary-and-budget-for-it)).
- `--max-time 900`: one long page can take several minutes.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for. Input is $0.07 per million tokens, output $0.281 per million, and cached input $0.003 per million; prices are on the [model page][model].
- Optional fields from the input schema: `temperature` (0 to 2), `response_format`, `stop` and `stream`.
- Images work the same way: the model accepts image input, so you can put a reference image in `messages[].content` instead of describing it.

Open `hy4-flash.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (simplify the brief or split the scene) or a CDN that did not load (ask for everything inline).

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect tencent/hy4-flash   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 64000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_tencent_hy4_flash -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs hy4-flash.html hy4-flash.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a fixed-length loop (see [prompt guide §4](prompt-guide.md)), so nothing depends on a mouse.

The recording is picture only, so add audio in the edit. If you record the page yourself, capture the tab audio, not the microphone.

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Hy4 Flash. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-hy4-flash/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/hy4-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[arena]: https://www.sandbase.ai/arena/text?models=tencent%2Fhy4-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[model]: https://www.sandbase.ai/model/tencent/hy4-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-hy4-flash
