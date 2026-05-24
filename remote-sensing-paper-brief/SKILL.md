---
name: remote-sensing-paper-brief
description: Generate a structured Chinese Markdown note package from remote sensing method-paper PDFs according to the user's preferred reading habits. Use when the user asks in Chinese or English to read, summarize, analyze, or extract key points from a remote sensing method paper, 遥感方法类论文, 论文PDF, paper brief, or paper note, especially papers on semantic segmentation, object detection, scene classification, change detection, crop mapping, crop yield estimation, and related ML/DL applications. Less suitable for application-oriented, discovery-oriented, review, or theory papers. Trigger for 按我的阅读习惯读论文, 生成论文要点集合, 提取遥感论文重点, 整理成md笔记, 读这篇PDF, or summarize this remote sensing method paper. Create a short slug-named note folder, same-slug Markdown file, and ./figures for workflow/architecture images. Extract task/problem/gap/contributions, study area or datasets, data sources, figures, experiments/results, discussion, limitations, and future work.
---

# Remote Sensing Paper Brief

## Overview

Use this skill to read a remote sensing method paper PDF in the user's preferred order and produce a concise Chinese Markdown note package. Prioritize method understanding, data context, workflow/architecture figures, experiments, and reusable research insights over full-paper translation.

This skill is mainly designed for remote sensing method papers. It may be less suitable for application-oriented papers, discovery-oriented studies, review papers, policy papers, or theory papers, because their structure may not center on a reusable method workflow, architecture, datasets, and experiments.

## Required Output

Use `references/brief-template.md` as the default structure unless the user provides a different format. Keep the report concise, but preserve exact technical names, dataset names, sensor/product names, model names, metrics, and numeric results.

Use Chinese as the main narrative language. Avoid unnecessary Chinese-English mixing. Translate ordinary prose, section explanations, experiment descriptions, and discussion points into natural Chinese.

Keep English only for official paper titles, dataset names, model/module/method names, product names, software/platform names, sensor names, metric abbreviations, and terms whose English form is a named concept in the paper. For common technical terms, use Chinese first and optionally keep English in parentheses on first mention; after first mention, prefer the Chinese term unless the English term is a proper noun or clearer.

Use `references/remote-sensing-glossary.md` for common remote sensing and machine-learning term translations when wording matters. When a term appears in the glossary, use the glossary translation by default. Do not replace it with another common translation unless the user explicitly asks or the paper defines a different official Chinese term. Do not force every English term into Chinese if the glossary or paper context suggests preserving the original name.

For each major section of the note, include source anchors from the paper whenever available: section name, page number, figure number, or table number. Use `Source:` lines or source columns in tables. This is required for background/significance, prior-study limitations, research content, contributions, study area/data, method figures, method explanation, experiment results, discussion topics, limitations, and future work.

Use Chinese-only wording for user-facing section headings where natural. In particular, avoid English in headings for the research problem/gap/contribution section, the method section, method subsections, and the discussion section. Keep English terms inside body text only when they are official names, abbreviations, or clearer technical terms.

## Python Dependency Setup

Before reading a PDF with Python, check whether the needed packages are installed. Use:

```bash
python <skill-dir>/scripts/setup_deps.py
```

This installs packages from `scripts/requirements.txt` when they are missing. If installation fails because package downloads require network access, ask for approval and rerun the same setup command according to the active environment's permission rules.

Use these packages for PDF work:

- PyMuPDF (`fitz`) for reliable page rendering and figure screenshots.
- `pdfplumber` or `pypdf` for text extraction, section discovery, and page-level inspection.
- Pillow for image format checks and conversions.

## File Layout

Create the note package under the current project/workspace directory unless the user specifies another destination.

In the final Markdown note, record only the PDF filename or a workspace-relative path. Do not record local absolute paths, usernames, home directories, or other machine-specific path details.

Use a short slug from the first several meaningful words of the original paper title as both the folder name and Markdown filename. Join words with hyphens and use lowercase English when possible:

```text
<short-title-slug>/
  <short-title-slug>.md
  figures/
    <figure images>
```

Choose enough words to identify the paper without making the path long, usually 4-8 title words. Drop leading articles and generic filler words when helpful. Sanitize characters that are invalid for the local filesystem, such as `\ / : * ? " < > |` on Windows. Record the full original title inside the Markdown note.

Examples:

- `Phenology-assisted supervised paddy rice mapping with the Landsat imagery on Google Earth Engine Experiments in Heilongjiang Province of China from 1990 to 2020` -> `phenology-assisted-supervised-paddy-rice-mapping`
- `A deep learning framework for remote sensing image semantic segmentation` -> `deep-learning-framework-remote-sensing`

Store all captured workflow/architecture figures in `./figures/` relative to the Markdown file. Reference them in the Markdown with relative paths, for example:

```markdown
![Fig. 2 Overall workflow](./figures/fig2_overall_workflow.png)
```

Do not place extracted figures beside the PDF or in a global output directory unless the user explicitly asks.

## Reading Workflow

### 1. Identify the paper task

Read the title and abstract first. Extract the broad task/theme, such as:

- deep-learning semantic segmentation
- object detection
- scene classification
- change detection
- crop mapping
- crop yield estimation
- land-cover or land-use mapping
- retrieval, fusion, downscaling, transfer learning, foundation models, or other remote sensing method tasks

State the task in one sentence, then name the concrete target objects, classes, regions, or prediction variable when available.

### 2. Extract overview, prior-study limitations, research content, and contributions

Read the Introduction for:

- research background and significance
- limitations of existing studies
- what the paper proposes or studies
- the paper's explicitly stated contributions, innovations, or main contributions

In the final note, section 2 must be named `概述` and use this structure:

- `2.1 研究背景与意义`: one concise sentence only.
- `2.2 已有研究的不足`: summarize the limitations or gaps stated by the paper.
- `2.3 研究内容`: usually based on explicit wording such as "we propose...", "this study proposes...", or "we develop..."; translate and briefly restate it in one concise sentence, staying close to the paper's wording.
- `2.4 本文的贡献`: if the paper explicitly lists contributions, innovations, or main contributions, preserve the exact number of listed items and briefly translate/summarize each item without changing the count. If the paper does not explicitly list contributions, label the subsection as a summary by the reader/agent and summarize cautiously from the Introduction.

### 3. Extract study area, time range, datasets, and data

Read sections titled Materials, Study Area, Data, Dataset, Experimental Setup, or similarly named sections.

For application papers using traditional machine learning or deep learning, identify:

- study area / spatial scope
- study period / temporal range
- target classes, samples, field plots, administrative units, or observation units
- satellite data, statistical data, field survey data, remote sensing products, meteorological data, DEM, soil data, street-view/UAV/SAR/LiDAR data, or other inputs

For algorithm papers benchmarked on datasets, identify:

- public datasets used
- whether the paper created a new dataset
- dataset scale, classes, spatial resolution, modality, and train/validation/test split when easy to find

### 4. Capture technical-route and architecture figures

Find figures in Method, Methodology, Proposed Method, Framework, Network Architecture, or related sections.

Capture and save only figures that describe the technical route, workflow, model architecture, or method modules. The number of saved figures is variable:

- the overall workflow or technical route figure
- the model architecture figure
- important module-level or component-detail architecture figures, if present

Usually there may be one overall figure, but some papers include several figures: one overall pipeline plus detailed submodule diagrams. Save all method-relevant figures and do not assume there must be exactly two.

Do not save ordinary experimental result figures, statistical charts, accuracy bar charts, confusion matrices, qualitative result maps, sample visualization figures, or comparison plots unless the figure also directly explains the method workflow or architecture.

Name saved images clearly inside `./figures/`, for example `fig2_overall_workflow.png`, `fig3_model_architecture.png`, or `fig4_attention_module.png`. In the Markdown note, embed the images with relative paths and explain what each figure represents. If multiple method figures exist, distinguish the overall pipeline from submodule diagrams.

Do not rely only on figure captions when the figure contains essential method structure. Inspect the image content directly when possible.

Prefer page rendering over raw embedded-image extraction. Many paper figures are vector graphics or have transparent layers; extracting embedded images directly can produce black backgrounds, inverted colors, missing text, or unreadable/garbled labels. Render the PDF page or figure region as an RGB PNG with a white background, then crop the method figure.

Use `scripts/render_pdf_region.py` when useful:

```bash
python <skill-dir>/scripts/render_pdf_region.py paper.pdf --page 6 --out "<note-folder>/figures/fig4_framework.png" --dpi 240
python <skill-dir>/scripts/render_pdf_region.py paper.pdf --page 6 --crop x0,y0,x1,y1 --out "<note-folder>/figures/fig4_framework.png" --dpi 240
```

After saving each figure, open or inspect it before finalizing. Reject and regenerate figures that have black/inverted backgrounds, unreadable text, severe cropping, wrong figure content, or obvious rendering artifacts. The final image should match the PDF page visually and remain readable in the Markdown note.

Do not write internal processing notes in the final Markdown, such as which script was used, which page region was cropped, whether the image was checked as RGB/white-background, or which non-method result figures were deliberately excluded. The final note should contain only paper-grounded content and the saved method figures.

### 5. Explain the method

Read the Method/Methodology section and explain:

- overall workflow in order
- major modules and their inputs/outputs
- model backbone, fusion strategy, attention mechanism, loss function, feature pyramid, temporal module, or other key design when relevant
- what is actually novel versus reused from prior work

Keep this section detailed enough that the user can retell the method, but avoid line-by-line derivations unless the user asks.

In the final Markdown note, merge the technical-route figures and method explanation under one section named `方法`. Put the overall technical-route or workflow figure first, then write `方法总述`. If there are multiple method figures, place the overall figure first, then the overall explanation, then each module/detail figure followed immediately by its own explanation. Do not separate figures into a standalone figure-only section.

For deep-learning papers, summarize the loss function without overloading the brief. Keep the total loss formula when the paper provides one. If the total loss is composed of several smaller losses, do not reproduce every detailed sub-loss formula unless essential; use short labels for each component and explain in one concise sentence what each component encourages or penalizes. If the paper states weights for the loss components, list the specific weight values used in the paper.

### 6. Summarize experiments and accuracy results

Read Results, Experiments, Evaluation, and Ablation sections. Briefly list:

- comparison experiments and main baselines
- ablation experiments
- sensitivity/generalization/transfer experiments
- visualization or case-study experiments
- main accuracy metrics and results for each experiment

Do not reproduce detailed experimental settings unless necessary to interpret the result. Prefer compact tables or bullet lists.

### 7. Summarize discussion, limitations, and future work

Read Discussion. If Discussion is absent, inspect the end of Results and Conclusion.

Only list the discussion topics. Explain details only when the paper reports a counterintuitive, surprising, or especially useful conclusion.

Extract:

- limitations acknowledged by the authors
- future work proposed by the authors
- reader-facing concerns or caveats that matter for reusing the method

## Quality Rules

- Ground every major claim in the PDF section where it was found.
- Answer strictly according to the paper content. Do not invent tasks, datasets, numbers, conclusions, limitations, or future work.
- Mark missing information as "未明确说明" instead of guessing.
- If a statement is inferred rather than explicitly stated, label it as "推断" and explain the basis briefly.
- Do not fill template cells with plausible domain defaults. Leave them as "未明确说明" when the paper does not provide the information.
- Attach source anchors to extracted facts. Prefer precise anchors such as `Abstract`, `Introduction p.2`, `Fig. 4`, or `Table 3`; use broader anchors only when exact pages or numbers are unavailable.
- Preserve page/figure/table numbers when available.
- Prefer exact metric names and numeric values over vague statements like "效果较好".
- Distinguish "dataset" from "data source"; a paper may use public datasets, self-built datasets, and raw satellite/statistical/field data at the same time.
- Mention whether the paper is mainly an algorithm benchmark paper, a regional application paper, or a hybrid of both.
- Keep the final brief focused; do not produce a full translation unless explicitly requested.

## Deliverables

Return:

1. A short slug-named folder in the project directory.
2. A Markdown note inside that folder using the same slug filename and following the template.
3. Technical-route/workflow/architecture figure images saved under `./figures/` and embedded in the Markdown with relative paths.
4. A short note listing any sections, figures, or values that could not be confidently extracted.
