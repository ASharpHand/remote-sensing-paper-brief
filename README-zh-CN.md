# Remote Sensing Paper Brief

中文 | [🔗 English](README.md)

这是一个 Codex skill，用于阅读遥感方法类论文 PDF，并按照固定阅读习惯生成结构化中文 Markdown 笔记。

该 skill 主要面向遥感方法类论文。

本 skill 主要适用于遥感方法类论文。对于偏应用型、发现型、综述型、政策型或理论型论文不太适用，生成结果可能会出现结构不匹配、信息缺失或表述别扭等问题。

## 输出内容

每篇论文会生成一个短 slug 命名的笔记文件夹：

```text
<short-title-slug>/
  <short-title-slug>.md
  figures/
    <method-figure-images>.png
```

笔记重点包括：

- 本文任务
- 概述、研究背景、已有研究不足、研究内容和贡献
- 研究区、时间范围、数据集和数据来源
- 方法技术路线、模型架构、模块说明和损失函数摘要
- 实验与精度结果
- 讨论、局限与未来工作
- 关键事实的论文来源锚点

只保存方法相关图片，例如技术路线图、工作流图、模型架构图和模块结构图。普通结果图、统计图、混淆矩阵、定性结果图等不会保存，除非它们同时解释了方法流程或结构。

## Skill 结构

```text
remote-sensing-paper-brief/
  README.md
  README-zh-CN.md
  GETTING-STARTED-zh-CN.md
  remote-sensing-paper-brief/
    SKILL.md
    agents/
      openai.yaml
    references/
      brief-template.md
      remote-sensing-glossary.md
    scripts/
      render_pdf_region.py
      requirements.txt
      setup_deps.py
```

## 安装

新手推荐方式：

1. 下载整个仓库。
2. 在 Codex App 中打开下载后的文件夹。
3. 告诉 Codex：`这个仓库的内层 remote-sensing-paper-brief 文件夹是 Codex skill，请帮我安装到本机 Codex skills 目录，并校验是否可用。`

手动安装方式：

将内层 skill 文件夹复制到 Codex skills 目录：

```text
<本仓库>/remote-sensing-paper-brief -> ~/.codex/skills/remote-sensing-paper-brief
```

Windows 上通常是：

```text
<本仓库>/remote-sensing-paper-brief -> C:/Users/<username>/.codex/skills/remote-sensing-paper-brief
```

## Python 依赖

该 skill 需要 Python 3.10 或更高版本。它包含用于 PDF 文本读取支持和方法图渲染的辅助脚本。

检查并安装依赖：

```bash
python remote-sensing-paper-brief/scripts/setup_deps.py
```

依赖列表位于：

```text
remote-sensing-paper-brief/scripts/requirements.txt
```

## 使用方式

显式调用：

```text
Use $remote-sensing-paper-brief to read this remote sensing method paper PDF and create a structured Markdown note.
```

自然语言调用示例：

```text
帮我按我的阅读习惯读这篇遥感方法类论文，生成 md 笔记。
```

```text
整理这篇遥感论文的要点集合，保存方法图。
```

## 注意事项

- 生成笔记必须严格依据论文内容。
- 未能确认的信息应标记为 `未明确说明`。
- 推断性内容应标记为 `推断`，并简要说明依据。
- `remote-sensing-paper-brief/references/remote-sensing-glossary.md` 中的术语翻译默认优先使用。

## 新手指南

如果你是第一次使用 Codex skill，可以阅读 [🔗 从 0 开始使用 Remote Sensing Paper Brief](GETTING-STARTED-zh-CN.md)。这份指南会从安装 Codex 开始，介绍如何安装本 skill、准备论文 PDF、生成第一份 Markdown 笔记，以及处理常见问题。

## 致谢

特别感谢 [Zhewei Zhang](https://github.com/Ar9av/PaperOrchestra) 为本项目提供宝贵的产品反馈、功能建议和测试支持。

## 反馈

如果你有任何需求、建议或问题，欢迎提交 issue。
