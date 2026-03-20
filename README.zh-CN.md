# Write-Claw

<div align="center">
  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
    <img src="https://img.shields.io/badge/FastAPI-本地%20Web%20门户-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI 门户">
    <img src="https://img.shields.io/badge/模式-Local%20First-2563EB?style=for-the-badge" alt="Local First">
    <img src="https://img.shields.io/badge/工作台-Claw%20Native-7C3AED?style=for-the-badge" alt="Claw Native">
  </p>

  <h3>✨ 一个面向长篇 AI 写作的 Claw 原生工作台：可见运行轨迹、可编辑记忆面板、可中断章节检查点。</h3>

  <p>
    💡 Write-Claw 不是“输入一句提示词，返回一段文本”的壳，而是一个真正可操作、可观察、可干预的写作工作空间。
  </p>

  <p>
    <a href="./README.md"><img src="https://img.shields.io/badge/English-README-ef4444?style=flat-square" alt="English README"></a>
    <a href="./local_web_portal/start_local.ps1"><img src="https://img.shields.io/badge/本地启动-PowerShell-0f766e?style=flat-square&logo=powershell&logoColor=white" alt="本地启动"></a>
    <a href="./local_web_portal/README.md"><img src="https://img.shields.io/badge/Portal-部署说明-f59e0b?style=flat-square&logo=readthedocs&logoColor=white" alt="Portal 部署说明"></a>
    <a href="./EXPORT_WHITELIST.md"><img src="https://img.shields.io/badge/GitHub-导出白名单-1d4ed8?style=flat-square&logo=github&logoColor=white" alt="导出白名单"></a>
  </p>

  <p>
    <a href="#概览">概览</a> |
    <a href="#视觉预览">视觉预览</a> |
    <a href="#为什么它不一样">为什么它不一样</a> |
    <a href="#快速开始">快速开始</a> |
    <a href="#集成包">集成包</a> |
    <a href="#仓库结构">仓库结构</a>
  </p>
</div>

<p align="center">
  <img src="png/2.png" alt="Write-Claw 主工作台预览" width="100%">
</p>

> 🚀 **本地演示入口**
> 直接运行 **[`.\local_web_portal\start_local.ps1`](./local_web_portal/start_local.ps1)**，然后访问 `http://127.0.0.1:8010`。

## 概览 🌟

`Write-Claw` 是一个面向长篇 AI 写作的运行时工作台。它不把写作看成单次问答，而是把本地 Web 门户、Claw 风格调度循环、可编辑记忆面板、章节 checkpoint 和可见执行轨迹整合进同一个连续工作流里。

它尤其适合这些人：

- 📚 想按章节推进，而不是一次性生成整篇内容的写作者
- 👀 想看见系统在做什么，而不是只看最终输出的用户
- 🧠 需要持续维护角色状态、世界规则、修订笔记和记忆资产的创作者
- 🤝 希望人在回路中，能随时中断、改方向、继续推进的协同写作场景
- 🛠️ 想把同一套写作流程分发到 Claude / Codex 宿主中的开发者

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>👀 可见运行轨迹</h3>
      <p>你可以看到当前执行步骤、运行流和工作进度，而不是面对一个黑箱。</p>
    </td>
    <td width="33%" valign="top">
      <h3>🧠 可编辑记忆面板</h3>
      <p>角色状态、世界设定、写作笔记和连续性信息可以持续保留，并以面板形式编辑。</p>
    </td>
    <td width="33%" valign="top">
      <h3>📍 章节检查点</h3>
      <p>每一章都可以成为一个可暂停、可检查、可重定向的决策节点，而不是被动接受生成结果。</p>
    </td>
  </tr>
</table>

## 视觉预览 👀

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="png/1.png" alt="Write-Claw 运行轨迹预览" />
    </td>
    <td width="50%" valign="top">
      <img src="png/3.png" alt="Write-Claw 章节推进预览" />
    </td>
  </tr>
</table>

Write-Claw 的核心理念很直接：AI 写作应该从头到尾都能被观察、打断、修改，并且真正具备记忆能力。✨

## 为什么它不一样 ✨

| 常见写作工具 | Write-Claw |
|---|---|
| 主要只展示最终输出 | 展示运行轨迹、步骤、checkpoint 和工作区状态 |
| 写作体验更像一条长聊天记录 | 写作体验更像一个可管理的章节工作台 |
| 记忆常常是隐式的 | 记忆面板、设定和笔记可以保持可见且可编辑 |
| 很难中途暂停和改向 | 天生支持中断、调整和章节级控制 |
| 宿主复用能力有限 | 自带 Claude / Codex 两种分发包 |

### 核心体验 🧩

| 模块 | 作用 |
|---|---|
| `Runtime Loop` | 提供可见的 Claw 风格执行循环和运行流 |
| `Writing Console` | 把对话、进度、正文和运行状态放进同一个工作面 |
| `Memory Surface` | 承载 canon、角色状态、世界事实和修订笔记 |
| `Workspace Tools` | 把规划、同步、检索、修订和章节操作放到一个工作台里 |

## 界面画廊 🖼️

### 运行与推进

<table>
  <tr>
    <td width="33%">
      <img src="png/1.png" alt="运行轨迹" />
      <p align="center"><sub>实时运行轨迹</sub></p>
    </td>
    <td width="33%">
      <img src="png/2.png" alt="主工作台" />
      <p align="center"><sub>主工作台界面</sub></p>
    </td>
    <td width="33%">
      <img src="png/3.png" alt="章节推进" />
      <p align="center"><sub>章节推进流程</sub></p>
    </td>
  </tr>
</table>

### 资产与故事工作区

<table>
  <tr>
    <td width="33%">
      <img src="png/4.png" alt="角色档案" />
      <p align="center"><sub>角色档案</sub></p>
    </td>
    <td width="33%">
      <img src="png/5.png" alt="世界与上下文视图" />
      <p align="center"><sub>世界与上下文视图</sub></p>
    </td>
    <td width="33%">
      <img src="png/6.png" alt="故事板工作区" />
      <p align="center"><sub>故事板工作区</sub></p>
    </td>
  </tr>
</table>

### 记忆、编辑与控制

<table>
  <tr>
    <td width="33%">
      <img src="png/7.png" alt="记忆总览" />
      <p align="center"><sub>记忆总览</sub></p>
    </td>
    <td width="33%">
      <img src="png/8.png" alt="可编辑工作区细节" />
      <p align="center"><sub>可编辑工作区细节</sub></p>
    </td>
    <td width="33%">
      <img src="png/9.png" alt="能力控制台" />
      <p align="center"><sub>能力控制台</sub></p>
    </td>
  </tr>
</table>

<details>
<summary><b>查看更多截图</b></summary>

<table>
  <tr>
    <td width="33%">
      <img src="png/10.png" alt="模型设置" />
      <p align="center"><sub>模型设置</sub></p>
    </td>
    <td width="33%">
      <img src="png/11.png" alt="会话中心" />
      <p align="center"><sub>会话中心</sub></p>
    </td>
    <td width="33%">
      <img src="png/12.png" alt="状态与轨迹" />
      <p align="center"><sub>状态与轨迹</sub></p>
    </td>
  </tr>
  <tr>
    <td width="33%">
      <img src="png/13.png" alt="技能与代理" />
      <p align="center"><sub>技能与代理</sub></p>
    </td>
    <td width="33%">
      <img src="png/14.png" alt="写作工作区" />
      <p align="center"><sub>写作工作区</sub></p>
    </td>
    <td width="33%">
      <img src="png/15.png" alt="系统能力栈" />
      <p align="center"><sub>系统能力栈</sub></p>
    </td>
  </tr>
</table>

</details>

## 适合谁用 🎯

- ✍️ 需要章节级控制的写作者
- 🤖 想研究 agent、工具、记忆系统和可见调度流程的开发者
- 🔬 关注长篇写作、人机协作和运行时交互的研究者

## 快速开始 🚀

<details open>
<summary><b>🌐 方案 A：直接启动本地 Web 门户</b></summary>

推荐命令：

```powershell
.\local_web_portal\start_local.ps1
```

这个脚本会：

- ✅ 自动创建 `.venv`
- ✅ 安装根目录和 portal 依赖
- ✅ 自动从 `.env.example` 创建 `local_web_portal\.env`
- ✅ 在 `127.0.0.1:8010` 启动应用

访问地址：

```text
http://127.0.0.1:8010
```

</details>

<details>
<summary><b>⌨️ 方案 B：手动安装与启动</b></summary>

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m pip install -r local_web_portal\requirements.txt
Copy-Item local_web_portal\.env.example local_web_portal\.env
python -m uvicorn local_web_portal.app.main:app --host 127.0.0.1 --port 8010
```

</details>

### 默认导出行为

GitHub 导出版本默认以“无模型工作台模式”启动：

```text
WEB_MODELLESS_MODE=1
DISABLE_EMBEDDING_DOWNLOADS=1
```

这意味着：

- 🌐 portal 可以在没有 provider 配置的情况下启动
- 🔐 登录、浏览工作区和查看本地状态不依赖 API Key
- 📦 导出版默认禁用 RAG embedding 下载
- 🧪 只有你显式设置 `WEB_MODELLESS_MODE=0` 之后，才会打开真实模型驱动生成

### 超时设置

如果你希望长任务不被超时截断，请在 `local_web_portal\.env` 中保留：

```text
WEB_JOB_TIMEOUT_SECONDS=0
WEB_JOB_IDLE_TIMEOUT_SECONDS=0
LLM_TIMEOUT_SECONDS=0
```

## 部署说明 🛠️

### 本地部署

- 优先使用 `.\local_web_portal\start_local.ps1`
- 如果你想手动启动，可使用 `python -m uvicorn local_web_portal.app.main:app --host 127.0.0.1 --port 8010`
- 长任务运行时，不建议随便打开 `--reload`

### 服务器部署

最小生产式启动命令：

```bash
uvicorn local_web_portal.app.main:app --host 0.0.0.0 --port 8010 --workers 2
```

建议配置这些环境变量：

- `APP_SESSION_SECRET`
- `APP_ENCRYPTION_KEY`
- `APP_HTTPS_ONLY=1`
- 多用户生产部署时使用 `APP_DATABASE_URL` 切换到 PostgreSQL

详见 [local_web_portal/README.md](./local_web_portal/README.md)。

## 集成包 🔌

Write-Claw 自带两种宿主分发方式：

- `integrations/claude-plugin-bundle`
  面向 Claude 的 `.claude-plugin` 风格分发包
- `integrations/codex-skill-bundle`
  面向 Codex 的 `AGENTS.md + .codex/skills` 风格分发包

这些分发包 **不要求 MCP**。

如果你主要需要的是：

- 可复用 prompt
- 章节工作流结构
- 连续性和记忆约定
- 宿主特定的安装布局

那就可以直接用这些包；只有当你需要统一的工具调用层时，再考虑接入 MCP。

## Release 包 📦

仓库已经自带预打包的 release 产物：

- [release/write-claw-claude-plugin.zip](./release/write-claw-claude-plugin.zip)
- [release/write-claw-codex-skill.zip](./release/write-claw-codex-skill.zip)
- [release/release-notes-v0.1.0.md](./release/release-notes-v0.1.0.md)

如果后续发布 GitHub Release，这两个 zip 文件就是最适合上传的资产。

## 仓库结构 🗂️

```text
Write-Claw/
|-- agents/                # agent 实现
|-- rag/                   # 记忆与检索
|-- utils/                 # 通用工具
|-- workflow/              # 调度与执行
|-- local_web_portal/      # FastAPI 门户和启动脚本
|-- integrations/          # Claude / Codex 复用包
|-- release/               # 已打包的 release 资产
|-- png/                   # README 截图资源
|-- capability_registry.py # 能力注册表
|-- config.py              # 配置中心
|-- main.py                # 主运行入口
`-- requirements.txt       # 依赖列表
```

## 更多文档 📚

- 🇬🇧 英文 README: [README.md](./README.md)
- 🌐 Portal 部署说明: [local_web_portal/README.md](./local_web_portal/README.md)
- 📦 GitHub 导出白名单: [EXPORT_WHITELIST.md](./EXPORT_WHITELIST.md)
- 🔌 集成包说明: [integrations/README.md](./integrations/README.md)
