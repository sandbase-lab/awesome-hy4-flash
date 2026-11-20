"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'hy4-flash'
REPO = 'sandbase-lab/awesome-hy4-flash'

CFG = dict(
    slug=SLUG,
    name='Hy4 Flash',
    short='Hy4 Flash',  # how the prose refers to the model after the first mention
    vendor='Tencent Hunyuan',
    model_id='tencent/hy4-flash',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-hy4-flash',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/tencent/hy4-flash',
    arena=f'{SITE}/arena/text?models=tencent%2Fhy4-flash',
    evals=f'{SITE}/leaderboards',
    pelican=f'{SITE}/arena/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-hy4-flash-sync/1.0 (+https://github.com/{REPO})',
    html_out='hy4-flash.html',
    # Output limit for the curl example. `sandbase inspect tencent/hy4-flash --json` caps
    # max_tokens at 64,000, so the example asks for that maximum.
    max_tokens=64000,
    max_tokens_limit=64000,
    context_length=1048576,
    guide_patterns=6,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Hy4 Flash',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'argon', 'deepseek', 'kimi', 'grok', 'qwen', 'glm', 'hy4'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Tencent Hunyuan.',
                    'zh-CN': '与腾讯混元（Tencent Hunyuan）无隶属或背书关系。'},
    # No SandBase blog post on Hy4 Flash is listed in the source bundle. build_readme.py skips the
    # reading section while this is empty; do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect tencent/hy4-flash`, the Lab collection's own posts
# (linked), and the creator posts quoted in docs/model-comparison.md. No Lab Evals or Pelican Test
# row for Hy4 Flash is in the source bundle, so the copy says so rather than inventing one.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Hy4 Flash examples**: videos, prompts and demos made with Hy4-Flash, the cost-efficient tier of Tencent Hunyuan\'s Hy4 family, announced on November 16, 2026. Three.js and SVG scenes, 2D animation, 3D models, browser platformers and playable games, most of them written as one self-contained HTML page from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome Hy4 Flash: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[Hy4 Flash vs. DeepSeek V4.1 Flash 1017, Claude Opus 5.5 and Hy4](docs/model-comparison.md)'),
            ('Try it now', '[Run Hy4 Flash in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. `max_tokens` is capped at 64,000 for this model, so the call above asks for that maximum. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Hy4 Flash?', 'Hy4-Flash is the cost-efficient tier of Tencent Hunyuan\'s Hy4 family, announced on November 16, 2026, with roughly a quarter of the flagship\'s parameters. It accepts text and image input, has a context window of about 1,048,576 tokens, and supports reasoning, tool calling and structured output. On SandBase it is `{model_id}`, priced at $0.07 per million input tokens and $0.281 per million output tokens. Source: `sandbase inspect tencent/hy4-flash`.'),
            ('How are these Hy4 Flash videos made?', 'The model doesn\'t render video. It writes a web page (HTML with Three.js, SVG, Canvas or CSS animation), and the creator records the page playing. Creators ran it one-shot, without a harness, and some compared it against other models on the same prompt. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Hy4 Flash prompt?', 'Name one self-contained HTML file and the renderer you want (Three.js, SVG, Canvas or CSS), describe the subject and the motion, and ban external assets. Creators who shared prompts kept them to one concrete subject, such as a mechanical dragonfly or a keyboard that disassembles layer by layer. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Hy4 Flash API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. One key works for every model. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Hy4 Flash better than DeepSeek V4.1 Flash 1017, Claude Opus 5.5 or Hy4?', 'There is no measured answer yet. The source bundle has no Lab Evals or Pelican Test row for Hy4 Flash, so no benchmark score is quoted here. The creator evidence is one-shot and mixed: one creator found DeepSeek V4.1 Flash 1017 more mechanical on a dragonfly test and said Hy4 Flash was more basic, while DesignArena reports that the larger Hy4 adds more detail on the same 3D prompt. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'The list price on SandBase is $0.07 per million input tokens, $0.281 per million output tokens, and $0.003 per million cached input tokens. Creators also report Hy4 Flash free in WorkBuddy. Reasoning tokens bill as output. Source: `sandbase inspect tencent/hy4-flash`.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Hy4 Flash creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Hy4 Flash prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Hy4 Flash videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Hy4 Flash 案例**合集：用 Hy4-Flash（腾讯混元 Hy4 系列中性价比更高的一档，2026 年 11 月 16 日发布）做出的视频、提示词和演示。包括 Three.js 与 SVG 场景、2D 动画、3D 模型、浏览器平台跳跃游戏和可以直接玩的游戏，大多是模型根据提示词写成的单文件网页，均注明作者并链接原帖。',
        'alt': 'Awesome Hy4 Flash：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[Hy4 Flash 对比 DeepSeek V4.1 Flash 1017、Claude Opus 5.5 和 Hy4](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Hy4 Flash]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。这个模型的 `max_tokens` 上限是 64000，所以上面的示例直接取该上限。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Hy4 Flash 是什么？', 'Hy4-Flash 是腾讯混元 Hy4 系列中性价比更高的一档，2026 年 11 月 16 日发布，参数量约为旗舰的四分之一。它接受文本和图片输入，上下文窗口约 1,048,576 token，支持推理、工具调用和结构化输出。在 SandBase 上它是 `{model_id}`，标价为每百万输入 token $0.07、每百万输出 token $0.281。来源：`sandbase inspect tencent/hy4-flash`。'),
            ('这些 Hy4 Flash 视频是怎么做出来的？', '模型并不直接渲染视频。它写出一个网页（用 Three.js、SVG、Canvas 或 CSS 动画的 HTML），作者再把页面播放过程录下来。有作者不用 harness、一次生成，也有作者在同一提示词下和其他模型对比。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Hy4 Flash 提示词？', '指定输出一个独立的 HTML 文件，并说明用哪个渲染方式（Three.js、SVG、Canvas 或 CSS）；描述主体和运动，禁止外部素材。公开提示词的作者大多只写一个具体主体，比如一只机械蜻蜓，或一个逐层拆解的键盘。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Hy4 Flash API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Hy4 Flash 比 DeepSeek V4.1 Flash 1017、Claude Opus 5.5 或 Hy4 更强吗？', '目前没有实测结论。来源资料里没有 Hy4 Flash 的 Lab Evals 或 Pelican Test 数据，所以这里不引用任何基准分数。创作者的证据是单次生成、且结论不一：一位作者在机械蜻蜓测试中认为 DeepSeek V4.1 Flash 1017 更有机械感，并称 Hy4 Flash 更简单；DesignArena 则报告，同一个 3D 提示词下，更大的 Hy4 细节更丰富。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', 'SandBase 标价为每百万输入 token $0.07、每百万输出 token $0.281，每百万缓存输入 token $0.003。也有创作者报告在 WorkBuddy 中免费使用 Hy4 Flash。推理 token 按输出计费。来源：`sandbase inspect tencent/hy4-flash`。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Hy4 Flash 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Hy4 Flash 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Hy4 Flash 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
