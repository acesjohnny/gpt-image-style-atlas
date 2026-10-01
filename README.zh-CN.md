# GPT Image 风格图鉴

**同一个画面，116 种画风。** GPT Image 2 风格对照卡，每张都配可直接复制的提示词。

[English](README.md) · [在线浏览](https://acesjohnny.github.io/gpt-image-style-atlas/) · [116 张风格卡](styles/README.md)

![116 张风格卡中的 12 张](assets/preview.jpg)

每张卡画的都是同一个题材：七岁小孩坐在窗边软垫上读绘本，身边一只小猫蜷着睡觉，午后阳光照进来。题材不变，只换风格，所以「工笔」「民国月份牌」「孔版印刷」「羊毛毡」到底长什么样，一比就清楚，写提示词前心里有数。

## 里面有什么

| 位置 | 内容 |
|---|---|
| [`styles/`](styles/README.md) | 116 张风格卡，分 9 组：中国传统、民国与近代、手绘、绘画与艺术流派、版画与印刷、卡通与动漫、3D 与手作材质、摄影与影视、设计与图解 |
| [`styles/prompts.md`](styles/prompts.md) | 每张卡的完整提示词 |
| [`styles/styles.json`](styles/styles.json) | 同样的数据，方便程序读取 |
| [`docs/techniques.md`](docs/techniques.md) | 17 个出图脑洞技巧，从约 600 条公开的 GPT Image 2 案例里归纳，例图链接到原作者 |
| [`docs/case-index.md`](docs/case-index.md) | 626 条公开案例的标题、作者、原链接索引（只放链接，不转载图片和提示词） |
| [`tools/generate.py`](tools/generate.py) | 批量出图脚本：用 Codex CLI 的出图工具逐个风格出图，可断点续跑，额度用完自动停 |
| [`index.html`](index.html) | 可浏览的图鉴网页（搜索、按组筛选、点图复制提示词） |

## 套用某种风格

从卡片里复制「风格描述」，换成你自己的题材：

```text
Style: <风格描述>.
Subject: <你的题材>.
Render the whole image faithfully in this one style.
```

## 自己重新出图

```bash
python3 tools/generate.py --workers 3
```

需要安装 [Codex CLI](https://github.com/openai/codex) 并登录有出图功能的 ChatGPT 账号。出图额度和文字额度分开算，Plus 账号大约出 70 张就会用完；脚本会跳过已出好的图，额度恢复后再跑一次即可。

## 相关项目

想把图片做成视频？看 **[keyframe-video-skill](https://github.com/acesjohnny/keyframe-video-skill)**：关键帧驱动的 AI 视频制作 skill。

## 授权

代码：MIT。风格卡图片与文字：CC BY 4.0。部分风格名称借用艺术家或工作室作为风格参照，本项目与其无关联。`docs/case-index.md` 里列出的案例版权归原作者。
