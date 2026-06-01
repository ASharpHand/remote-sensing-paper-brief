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

Preserve mathematical notation throughout the entire final Markdown note. Optimize math output for common Markdown readers used by the user: VS Code, Obsidian, and Typora. This applies to all sections, tables, bullet lists, captions, method explanations, experiment metrics, formulas, variables, dimensions, units, thresholds, hyperparameters, and numeric expressions. When the paper contains symbols, formulas, variables, superscripts, subscripts, Greek letters, or metric expressions, write them as Markdown math instead of flattened plain text.

- Use single-dollar inline math for short symbols and values, because it is the most compatible inline style across VS Code math preview/extensions, Obsidian, and Typora. Examples: `$f_{\theta A}$`, `$x_i$`, `$R^2$`, `$10^{-4}$`, `$N \times C \times H \times W$`, `$\lambda_1$`, and `$m^2$`.
- Use double-dollar display math for standalone formulas when the formula is important enough to keep:

```markdown
$$
\mathcal{L}_{total}=\mathcal{L}_{ce}+\lambda\mathcal{L}_{dice}
$$
```

- Do not output flattened forms such as `f_thetaA`, `x_i` outside math mode, `R2`, `10-4`, `lambda1`, `m2`, or `N x C x H x W` when they represent mathematical notation.
- Do not use `\(...\)` inline delimiters in the final note unless the user explicitly asks for MathJax-style delimiters, because Typora and some VS Code setups may show them as raw text.
- Keep inline formulas compact and avoid spaces immediately inside the dollar delimiters: write `$p_i(c)$`, not `$ p_i(c) $`.
- When inline math appears next to Chinese or English punctuation, keep the punctuation outside the math delimiters: `类别 $c$，其中 $c \in \{1,\ldots,C\}$。`
- Escape literal braces inside set notation when needed, for example `$c \in \{1,\ldots,C\}$` instead of `$c\in{1,\ldots,C}$`.
- Avoid using dollar delimiters for currency or ordinary prose. If a literal dollar sign is needed, escape it as `\$`.
- If PDF text extraction flattens notation, reconstruct obvious Markdown math from the surrounding paper context whenever it can be done confidently.
- If the exact formula or symbol cannot be reconstructed confidently, describe it in words and mark the notation as uncertain instead of inventing a formula.

Keep English only for official paper titles, dataset names, model/module/method names, product names, software/platform names, sensor names, metric abbreviations, and terms whose English form is a named concept in the paper. For common technical terms, use Chinese first and optionally keep English in parentheses on first mention; after first mention, prefer the Chinese term unless the English term is a proper noun or clearer.

Use `references/remote-sensing-glossary.md` for common remote sensing and machine-learning term translations when wording matters. When a term appears in the glossary, use the glossary translation by default. Do not replace it with another common translation unless the user explicitly asks or the paper defines a different official Chinese term. Do not force every English term into Chinese if the glossary or paper context suggests preserving the original name.

For each major section of the note, include evidence anchors from the paper whenever available. Use only Chinese user-facing labels: write `依据：` lines after paragraphs or use a final table column named `依据`. Do not use `Source:`, `Source`, or mixed labels such as `Source / 推断依据` in the final note. Evidence anchors should follow these formats:

- Section anchors: use the paper's official section numbering at the smallest identifiable formal section level, such as `Abstract`, `Section 1`, `Section 3.2`, or `Section 4.1.2.3`. Do not artificially truncate the section level when the paper has deeper numbered subsections.
- Figure and table anchors: use only `Fig. X` or `Table X` when the source is a figure or table.
- Normalize section, figure, and table numbers to Arabic numerals in the final note whenever the conversion is reliable. For example, write `Section 4`, `Section 4.1`, `Section 4.1.2`, and `Table 1` instead of `Section IV`, `Section IV-A`, `Section IV-A-2`, and `Table I`. Figure numbers should also use Arabic numerals, but keep explicit subfigure labels when the paper itself names them, such as `Fig. 3 (a)` or `Fig. 3 (b)`. Do not invent subfigure labels from visual layout alone.
- Multiple anchors: separate them with Chinese semicolons, for example `依据：Section 3.2；Fig. 4；Table 2`.
- Forbidden final-note anchors: page numbers, PDF page positions, paragraph numbers, line numbers, crop regions, or wording such as `p.2`, `page 6`, `第 3 页`, `paragraph 2`, or `line 10`.

Evidence anchors are required for background/significance, prior-study limitations, research content, contributions, study area/data, method figures, method explanation, experiment results, discussion topics, limitations, future work, and data/code resource entries. For section 8 `数据与代码资源`, verify the evidence for each listed entry internally, but do not add an `依据` column to the section 8 tables unless the user explicitly asks for it.

Use Chinese-only wording for user-facing section headings where natural. In particular, avoid English in headings for the research problem/gap/contribution section, the method section, method subsections, and the discussion section. Keep English terms inside body text only when they are official names, abbreviations, or clearer technical terms.

## Python Dependency Setup

Before reading a PDF with Python, initialize or update the dedicated skill venv:

```bash
python <skill-dir>/scripts/setup_deps.py
```

The setup script creates or reuses a Python standard library `venv` at:

```text
~/.codex/skill-envs/remote-sensing-paper-brief/.venv
```
The venv must be created with Python 3.10 or later. If the default `python` is too old, the setup script tries common Python launcher commands such as `py -3.12`, `py -3.11`, `py -3.10`, `python3.12`, `python3.11`, and `python3.10`. A specific interpreter can also be provided with:

```bash
python <skill-dir>/scripts/setup_deps.py --python <path-to-python-3.10+>
```

After the environment exists, do not use bare `python` for bundled helper scripts. Resolve `<skill-python>` by using:

```text
Windows: ~/.codex/skill-envs/remote-sensing-paper-brief/.venv/Scripts/python.exe
macOS/Linux: ~/.codex/skill-envs/remote-sensing-paper-brief/.venv/bin/python
```

Use `<skill-python>` for all skill Python scripts, including PDF text extraction checks and figure rendering. If the venv is missing or packages are missing, rerun `python <skill-dir>/scripts/setup_deps.py`. If installation fails because package downloads require network access, ask for approval and rerun the same setup command according to the active environment's permission rules.

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

Include subsection `4.4 损失函数` only for papers that involve a deep-learning training framework. For non-deep-learning papers, delete the entire loss-function subsection from the final Markdown note; do not keep the heading and do not write a substitute explanation such as "本文不是深度学习训练框架" or a metric-based note. For deep-learning papers, summarize the loss function without overloading the brief. Keep the total loss formula when the paper provides one. If the total loss is composed of several smaller losses, do not reproduce every detailed sub-loss formula unless essential; use short labels for each component and explain in one concise sentence what each component encourages or penalizes. If the paper states weights for the loss components, list the specific weight values used in the paper.

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

### 8. Extract data and code resources

Create section 8 named `数据与代码资源` as a concise resource entry point for readers, not as another data-comparison or materials-analysis section. Use three subsections:

- `8.1 可复用数据来源`
- `8.2 本文产出数据`
- `8.3 代码资源`

Each subsection table must contain only these columns: `名称`, `类型`, and `链接或引用`. Do not add an `依据` column to these tables, even though every listed entry must be supported by the paper.

For `8.1 可复用数据来源`, list data resources that readers may need to trace, cite, download, or reuse, such as public datasets, public data products, statistical data, administrative or socioeconomic data, benchmark datasets, sample libraries, label sources, and other non-ordinary data resources. Do not list data access platforms or processing platforms themselves, such as Google Earth Engine, unless the platform page is the only paper-provided access point for a specific dataset or product. Do not list ordinary raw remote sensing imagery or standard imagery products such as routine Landsat, Sentinel, MODIS, or Landsat Level-2 SR entries by default, because readers generally know how to find them. Include remote sensing resources only when the paper uses a named dataset, benchmark, curated data product, published map product, or otherwise treats that resource as a key reusable dataset/product rather than ordinary imagery input. Do not list the authors' private field-survey or internal data by default in this subsection.

For `8.2 本文产出数据`, list data products created, constructed, generated, released, or provided by the paper, such as new datasets, labels, maps, prediction products, sample libraries, benchmark splits, supplementary datasets, regional products, or year-specific products. These signals may appear outside the data section, so specifically inspect the final sentences of the Abstract, the final paragraphs or contribution list of the Introduction, and the final paragraph of the Conclusion.

For `8.3 代码资源`, list only official code access points, such as code repositories, GitHub/GitLab links, GEE scripts, software packages, project pages, or supplementary-material code. Do not list model weights as a separate entry; if weights are part of the official code repository, the repository link is sufficient. If the paper states that code is available on request, not yet released, or unavailable, record that status concisely.

Use this search order for section 8:

1. Inspect the final sentences of the Abstract for release/provision signals such as datasets, data products, maps, code, or benchmarks.
2. Inspect the final paragraphs of the Introduction and any explicit contribution list for resources the authors construct, release, provide, or publish.
3. Inspect the final paragraph of the Conclusion for data, product, or code availability statements.
4. Inspect Data Availability, Code Availability, Data and Code Availability, Availability of data and materials, Supplementary Materials, Acknowledgements, and similar end-matter sections.
5. Search the extracted full text for link-like or repository terms such as `http://`, `https://`, `doi.org`, `github.com`, `gitlab`, `zenodo`, `figshare`, `dryad`, `osf`, `gee`, `code`, `dataset`, and `data availability`. For each hit, read the surrounding context and classify the link as reusable data, paper-produced data, code resource, software/tool reference, data or processing platform page, ordinary citation, or unrelated link.
6. Return to Data, Dataset, Materials, Experimental Setup, Methods, and Experiments sections to confirm how each candidate resource is used in the paper.
7. If a data resource has no URL/DOI/project link but the paper cites a data-product or dataset reference, find the corresponding item in References and copy the complete reference entry into `链接或引用`. Do not replace it with only an author-year shorthand or reference number.

For `链接或引用`, use this priority:

1. If the paper gives a URL, DOI, data portal, GitHub/GitLab repository, project page, or similar access point, write that link.
2. If no link is given but a data-product or dataset reference is given, copy the complete matching reference entry from the References section.
3. If only a name is given and no link or identifiable reference is available, write `未给出`.
4. Do not search the internet to add missing links unless the user explicitly requests external link completion.

If a subsection has no confirmed entries, write a single row such as `| 未明确说明 | | 未给出 |`. Do not invent resources or fill the tables with plausible domain defaults.

## Quality Rules

- Ground every major claim in the PDF section where it was found.
- Answer strictly according to the paper content. Do not invent tasks, datasets, numbers, conclusions, limitations, or future work.
- Mark missing information as "未明确说明" instead of guessing.
- If a statement is inferred rather than explicitly stated, label it as "推断" and explain the basis briefly.
- Do not fill template cells with plausible domain defaults. Leave them as "未明确说明" when the paper does not provide the information.
- Attach evidence anchors to extracted facts. Prefer precise anchors such as `Abstract`, `Section 2.1`, `Fig. 4`, or `Table 3`; use broader official section anchors only when exact numbered subsections, figures, or tables are unavailable.
- Preserve section/figure/table numbers when available, but do not include page, paragraph, line, or PDF-position anchors in the final note.
- Prefer exact metric names and numeric values over vague statements like "效果较好".
- Distinguish "dataset" from "data source"; a paper may use public datasets, self-built datasets, and raw satellite/statistical/field data at the same time.
- Keep section 8 focused on reusable data and code entry points. Do not duplicate every data source from section 3, do not list general platforms such as Google Earth Engine, and do not list ordinary raw remote sensing imagery or standard imagery products unless they are named datasets, benchmarks, curated data products, published map products, or key reusable resources in the paper.
- For section 8 references, copy the complete reference entry when a dataset or data product is cited without a direct link.
- Mention whether the paper is mainly an algorithm benchmark paper, a regional application paper, or a hybrid of both.
- Keep the final brief focused; do not produce a full translation unless explicitly requested.

## Deliverables

Return:

1. A short slug-named folder in the project directory.
2. A Markdown note inside that folder using the same slug filename and following the template.
3. Technical-route/workflow/architecture figure images saved under `./figures/` and embedded in the Markdown with relative paths.
4. A short note listing any sections, figures, or values that could not be confidently extracted.
