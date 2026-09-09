# 新手安装与上手指南（SETUP）

> 第一次使用本工作流？跟着这份指南走，5 分钟跑通。

## 0. 这个工作流是什么

把家人的检验报告照片/病历截图丢进 `原始资料/` 文件夹，对 AI（Kimi Code CLI）说一句 **"执行患者状态监测工作流"**，它会自动完成：

```
W1 资料摄取 → W2 状态评估 → W3 风险预警 → W4 家属报告 → W5 深度文献调研
```

产出一份家属能看懂的状态报告（MD + PDF），并存入结构化时间线供下次增量更新。

## 1. 前置要求

| 依赖 | 必需性 | 用途 |
|---|---|---|
| **Kimi Code CLI**（或任何能按提示词执行文件的 AI 编程助手） | ✅ 必需 | 执行工作流的"引擎" |
| **Python 3.8+** | ✅ 必需 | 读取检验报告 PDF、更新 JSON 时间线、生成 PDF 报告 |
| `pdfplumber` + `PyMuPDF (fitz)` | 推荐 | 提取检验报告 PDF 文本/图片 |
| `reportlab` | 推荐 | 把家属版报告转成 PDF |
| **PubMed Search MCP** | 可选 | W5 深度调研与文献 PMID 核实（无它 W5 会降级为纯经验总结） |

检查 Python 依赖：

```powershell
python -c "import pdfplumber, fitz, reportlab; print('全部就绪')"
```

缺失则安装：

```powershell
pip install pdfplumber PyMuPDF reportlab
```

## 2. 安装

```powershell
git clone https://github.com/784228565/patient-status-monitoring-workflow.git
cd patient-status-monitoring-workflow
python setup.py          # ← 初始化向导：建目录 + 检查环境
```

`setup.py` 会：
1. 创建 `data/`、`output/`、`原始资料/` 三个文件夹（已被 .gitignore 排除，不会误传）
2. 检查 Python 版本与可选依赖
3. 打印"下一步该做什么"

## 3. 首次使用

```
你的项目/
├── 患者状态监测工作流/    ← 本仓库内容放这里（或保持克隆目录原名）
└── 原始资料/             ← 检验报告照片、病历截图放这里
```

1. 把检验报告照片（.jpg/.png）、报告 PDF、家属观察记录（.txt）放入 `原始资料/`
2. 在 Kimi CLI 中打开项目目录，说：**"执行患者状态监测工作流"**
3. 查看产出：`患者状态监测工作流/output/患者状态报告_<日期>.md`（或 .pdf）

> 💡 目录名不限于"原始资料"——只要修改 `workflow.yaml` 和各 prompt 中的路径引用即可。

## 4. 常用模式

| 场景 | 对 AI 说 |
|---|---|
| 有新资料，完整更新 | "执行患者状态监测工作流" |
| 快速更新（跳过耗时文献调研） | "执行工作流，跳过W5" |
| 无新资料，仅重新分析 | "跳过W1，重新执行W2-W5" |
| 只用文献调研部分 | 复制 `prompts/W5_深度调研.md` 中"调研 Prompt 正文"到任意 Deep Research 工具 |

## 5. 使用前的两个准备动作

1. **填写患者问题清单**：`data/患者问题清单_<日期>.md` 是 W5 深度调研的输入框架——按模板 A 肿瘤本体 / B 治疗毒性 / C 合并症 / D 生活质量 四类列出你关心的问题。
2. **更新 W5 病例背景**：`prompts/W5_深度调研.md` 中的"病例背景"是示例快照，换成你自己患者的最新情况再用于独立调研。

## 6. 常见问题（FAQ）

**Q: 图片是斜着拍的，数值被认错了怎么办？**
A: 重新正拍；或在投喂前裁剪放大。工作流对可疑数值会标 `unclear` 而不会瞎猜，但最终以医院官方报告为准。

**Q: Windows 上中文文件名乱码？**
A: PowerShell 中加一行 `[Console]::OutputEncoding=[Text.Encoding]::UTF8`，或让 AI 用 Python 处理文件。

**Q: W5 报告说"文献未核实"？**
A: 说明 PubMed MCP 不可用。安装 pubmed-search MCP 后重新执行即可。

**Q: 可以分享/公开这个仓库吗？**
A: 可以——`workflow.yaml / prompts / schemas / README / SETUP` 均不含患者信息。但**永远不要**提交 `data/`、`output/`、`原始资料/`（`.gitignore` 已排除，提交前 `git status` 确认）。

## 7. 免责声明

本工作流输出仅供就医参考与家庭观察，不构成诊断或治疗建议。所有病情判断与用药以主治医生为准。
