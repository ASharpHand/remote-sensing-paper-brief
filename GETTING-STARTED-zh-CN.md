# 从 0 开始使用 Remote Sensing Paper Brief

[🔗 返回中文 README](README-zh-CN.md) | [🔗 English README](README.md)

这份文档面向完全没有使用过 Codex skill 的新手，目标是从安装 Codex App 开始，到使用本 skill 生成第一份遥感论文 Markdown 笔记。

> 说明：Codex 的安装和登录方式可能随官方更新变化。遇到差异时，以 OpenAI 官方文档为准：
>
> - [Codex App for Windows](https://developers.openai.com/codex/app/windows)
> - [Codex Windows setup guide](https://developers.openai.com/codex/windows)
> - [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)

## 1. 准备环境

你需要：

- 一个可用的 OpenAI / ChatGPT 账号
- Codex App
- Python 3.10 或更高版本
- 一个本地项目文件夹，用来保存论文 PDF 和生成的笔记

推荐额外安装：

- Git
- Node.js

它们不是本 skill 的核心依赖，但 Codex App 处理项目和运行工具时经常会用到。

## 2. 安装 Codex App

### 2.1 常规安装方式

在 Windows 上，Codex App 官方推荐通过 Microsoft Store 安装：

[Codex - Microsoft Store](https://apps.microsoft.com/detail/9plm9xgg6vks)

安装完成后，从开始菜单打开 `Codex`。

### 2.2 Microsoft Store 无法连接时的命令行安装方式

有些电脑上点击下载后会跳转或打开 Microsoft Store，但 Microsoft Store 可能连接失败、打不开、一直加载，或者受网络/系统策略影响不能正常安装。

这种情况下，可以用 PowerShell 走命令行安装。打开 PowerShell，运行：

```bash
winget install Codex -s msstore
```

这条命令仍然从 Microsoft Store 源安装 Codex App，但不需要你手动打开 Microsoft Store 图形界面。

如果提示找不到 `winget`，先更新 Windows，或安装/更新 Windows Package Manager。

安装完成后，从开始菜单打开 `Codex`。

### 2.3 更新 Codex App

常规更新方式：

- 打开 Microsoft Store
- 进入 `Downloads`
- 点击 `Check for updates`

如果 Microsoft Store 图形界面仍然不可用，可以再次尝试命令行方式：

```bash
winget upgrade Codex -s msstore
```

## 3. 登录 Codex App

首次打开 Codex App 时，按照界面提示登录你的 ChatGPT / OpenAI 账号。

如果你所在的账号套餐支持 Codex，登录后即可使用。不同套餐的额度和功能可能不同，以官方说明为准。

## 4. 配置 Codex App

在 Windows 上，Codex App 默认使用 Windows native agent，命令通常在 PowerShell 中运行。

建议先使用默认配置。后续如果你经常使用 Linux 工具链，再考虑把 agent 切换到 WSL。

如果你要处理本地项目，建议把项目放在普通 Windows 路径下，例如：

```text
E:/paper-notes/
```

## 5. 安装本 skill

### 5.1 推荐方式：让 Codex 帮你安装

对于新手，最简单的方式是：

1. 从 GitHub 下载整个仓库。
2. 解压到本地任意位置。
3. 在 Codex App 中打开或拖入这个下载后的仓库文件夹。
4. 对 Codex 说：

```text
这个仓库的内层 remote-sensing-paper-brief 文件夹是 Codex skill，请帮我安装到本机 Codex skills 目录，并校验是否可用。
```

Codex 会识别内层文件夹里的 `SKILL.md`，把这个真正的 skill 文件夹复制到本机 skills 目录，并运行校验。这样可以避免手动寻找 `.codex/skills` 路径。

### 5.2 手动安装方式

找到你的 Codex skills 目录。

常见位置：

```text
~/.codex/skills/
```

Windows 上通常是：

```text
C:/Users/<username>/.codex/skills/
```

将仓库内层的 `remote-sensing-paper-brief` skill 文件夹复制进去，最终结构应类似：

```text
C:/Users/<username>/.codex/skills/remote-sensing-paper-brief/
  SKILL.md
  agents/
  references/
  scripts/
```

## 6. 安装 Python 依赖

进入 skill 文件夹：

```bash
cd C:/Users/<username>/.codex/skills/remote-sensing-paper-brief
```

运行：

```bash
python scripts/setup_deps.py
```

这个命令会检测并安装 PDF 读取和图片渲染所需的 Python 包。

如果你在 Windows 上手动运行 skill 校验脚本，并遇到中文编码相关的 `UnicodeDecodeError`，先在同一个 PowerShell 窗口中启用 UTF-8 模式：

```powershell
$env:PYTHONUTF8=1
```

如果 PowerShell 提示脚本执行策略问题，或者 Codex App 无法运行 Python/pip，请参考官方 Windows setup/troubleshooting 文档。

## 7. 准备论文 PDF

建议新建一个工作目录，例如：

```text
E:/paper-notes/
```

把要阅读的遥感方法类论文 PDF 放进去。

第一次测试时，建议选择一篇你比较熟悉的论文，这样更容易判断生成结果是否符合你的阅读习惯。

## 8. 在 Codex App 中打开项目

打开 Codex App 后，添加或打开你的论文工作目录，例如：

```text
E:/paper-notes
```

## 9. 生成第一份论文笔记

在 Codex App 的对话框中输入类似请求：

```text
帮我按我的阅读习惯读这篇遥感方法类论文 PDF，生成 md 笔记，并保存方法图。
```

也可以显式调用 skill：

```text
Use $remote-sensing-paper-brief to read this remote sensing method paper PDF and create a structured Markdown note.
```

## 10. 查看输出结果

skill 会在当前项目目录下生成短 slug 命名的笔记文件夹：

```text
<short-title-slug>/
  <short-title-slug>.md
  figures/
    <method-figure-images>.png
```

打开 `.md` 文件，重点检查：

- 第 2 节“概述”是否准确
- 数据集和数据来源是否完整
- 方法图是否清晰、没有黑底或乱码
- 方法总述和模块分述是否能帮助你复述论文方法
- 实验结果是否有来源锚点
- 是否存在没有论文依据的推断

## 11. 常见问题

### Microsoft Store 打不开或连接失败

这是 Windows 上比较常见的安装阻碍。可以跳过 Microsoft Store 图形界面，直接在 PowerShell 中运行：

```bash
winget install Codex -s msstore
```

如果已经安装但需要更新，可以尝试：

```bash
winget upgrade Codex -s msstore
```

如果 `winget` 不可用，通常需要更新 Windows 或安装 Windows Package Manager。

### Codex 没有自动调用这个 skill

可以显式写：

```text
Use $remote-sensing-paper-brief ...
```

如果显式调用有效，说明 skill 本身可用；后续可以继续优化 `SKILL.md` 的 description 来改善自动触发。

### Python 依赖安装失败

通常是网络或权限问题。可以重新运行：

```bash
python scripts/setup_deps.py
```

如果 Codex 提示需要网络或权限批准，允许后再试。

### 方法图黑底、反色或文字不可读

本 skill 要求优先用 `scripts/render_pdf_region.py` 从 PDF 页面渲染 RGB 白底图片，而不是直接抽取 PDF 内嵌图片。

如果仍然出错，可以让 Codex 重新渲染对应页或调整裁剪区域。

### 笔记里出现不喜欢的翻译

优先修改：

```text
references/remote-sensing-glossary.md
```

如果是整体语言风格问题，再修改 `SKILL.md` 中的语言规则。
