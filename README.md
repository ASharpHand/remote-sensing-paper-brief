# Remote Sensing Paper Brief

[🔗 中文](README-zh-CN.md) | English

Codex skill for reading remote sensing method-paper PDFs and generating a structured Chinese Markdown note package.

This skill is mainly intended for remote sensing method papers.

It is less suitable for application-oriented papers, discovery-oriented studies, review papers, policy papers, or theory papers, and may produce incomplete or awkward notes for those paper types.

## What It Produces

For each paper, the skill creates a short slug-named note folder:

```text
<short-title-slug>/
  <short-title-slug>.md
  figures/
    <method-figure-images>.png
```

The note focuses on:

- paper task
- overview, background, prior-study limitations, research content, and contributions
- study area, time range, datasets, and data sources
- method workflow, architecture, module explanations, and loss function summary
- experiments and accuracy results
- discussion, limitations, and future work
- source anchors for key facts

Only method-related figures are saved, such as technical routes, workflows, architectures, and module diagrams. Ordinary result charts, statistical plots, confusion matrices, and qualitative maps are not saved unless they also explain the method structure.

## Skill Structure

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

## Installation

Beginner-friendly option:

1. Download this repository.
2. Open the downloaded folder in Codex App.
3. Ask Codex: `This repository contains a Codex skill in the inner remote-sensing-paper-brief folder. Please install that skill folder into my local Codex skills directory and validate it.`

Manual option:

Copy the inner skill folder into your Codex skills directory:

```text
<this-repository>/remote-sensing-paper-brief -> ~/.codex/skills/remote-sensing-paper-brief
```

On Windows, this is commonly:

```text
<this-repository>/remote-sensing-paper-brief -> C:/Users/<username>/.codex/skills/remote-sensing-paper-brief
```

## Python Dependencies

The skill requires Python 3.10 or later. It includes helper scripts for PDF text extraction support and robust figure rendering.

To check and install dependencies:

```bash
python remote-sensing-paper-brief/scripts/setup_deps.py
```

Dependencies are listed in:

```text
remote-sensing-paper-brief/scripts/requirements.txt
```

## Usage

Explicit invocation:

```text
Use $remote-sensing-paper-brief to read this remote sensing method paper PDF and create a structured Markdown note.
```

Natural-language invocation examples:

```text
帮我按我的阅读习惯读这篇遥感方法类论文，生成 md 笔记。
```

```text
整理这篇遥感论文的要点集合，保存方法图。
```

## Notes

- The generated note should be grounded strictly in the paper.
- Missing information should be marked as `未明确说明`.
- Inferred statements should be labeled as `推断` with a short basis.
- Glossary translations in `remote-sensing-paper-brief/references/remote-sensing-glossary.md` should be followed by default.

## Beginner Guide

If you are new to Codex skills, see [🔗 从 0 开始使用 Remote Sensing Paper Brief](GETTING-STARTED-zh-CN.md). It walks through installing Codex, installing this skill, preparing a PDF, generating the first Markdown note, and troubleshooting common issues.

## Acknowledgements

Special thanks to [Zhewei Zhang](https://github.com/Ar9av/PaperOrchestra) for valuable product feedback, feature suggestions, and testing support.

## Feedback

If you have any needs, suggestions, or problems, feel free to open an issue.
