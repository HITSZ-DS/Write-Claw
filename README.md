# Write-Claw

<div align="center">

**A claw-native workspace for long-form AI writing**  
**一个面向长篇 AI 写作的 Claw 原生工作台**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Portal-009688?style=flat-square&logo=fastapi&logoColor=white)
![Runtime](https://img.shields.io/badge/Runtime-Live%20Trace-2563EB?style=flat-square)
![Interaction](https://img.shields.io/badge/Interaction-Checkpoint%20%26%20Interrupt-7C3AED?style=flat-square)
![Language](https://img.shields.io/badge/Language-Chinese%20%2F%20English-111827?style=flat-square)

</div>

---

## Navigation

- [Installation](#installation)
- [Integrations](#integrations)
- [Plugin Usage](#plugin-usage)
- [Releases](#releases)
- [Repository Layout](#repository-layout)

Quick links:

- [Local startup](./local_web_portal/start_local.ps1)
- [Claude package source](./integrations/claude-plugin-bundle)
- [Codex package source](./integrations/codex-skill-bundle)
- [Claude release zip](./release/write-claw-claude-plugin.zip)
- [Codex release zip](./release/write-claw-codex-skill.zip)

## Opening | 开场一句话

Write-Claw is built around a simple idea: AI writing should not stop at "prompt in, text out."  
Write-Claw 围绕一个很直接的目标展开：AI 写作不该停留在“输入一句话，生成一段”。

It should be able to plan, write, pause, revise, remember, and keep the author inside the loop.  
它应该能够规划、写作、暂停、修订、记忆，并且始终把作者保留在创作循环里。

## Overview | 项目简介

`Write-Claw` is a runtime-focused writing workspace for long-form creation.  
It combines a local web portal, a Claw-style orchestration loop, editable memory surfaces, chapter checkpoints, and a visible execution trace into one continuous workflow.

`Write-Claw` 是一个面向长篇创作的运行时写作工作台。  
它把本地 Web 门户、Claw 风格调度循环、可编辑记忆面板、章节 checkpoint 和可见执行轨迹整合到同一个连续工作流中。

## Why It Gets Attention | 为什么它容易被关注

Most writing tools show only the output.  
Write-Claw tries to show the process.

大多数写作工具只展示结果。  
Write-Claw 更想把“过程”本身做出来。

- `Visible runtime`
  You can see what the system is doing instead of trusting a black box.
- `Interruptible flow`
  You can stop, steer, and adjust direction while the writing is still happening.
- `Checkpoint-driven chapters`
  Each chapter can become a decision point, not just a generated artifact.
- `Memory-first collaboration`
  Character state, world state, notes, and planning can accumulate over time.

## Core Experience | 核心体验

| Module | English | 中文 |
| --- | --- | --- |
| Runtime Loop | Dynamic Claw loop with live action trace and visible step flow. | 动态 Claw 循环，提供实时动作轨迹和可见步骤流。 |
| Writing Console | A unified surface for chat, progress, checkpoints, and manuscript work. | 统一界面整合对话、进度、checkpoint 和稿件工作区。 |
| Memory Surface | Editable panels for memory banks, character state, world facts, and revision notes. | 可编辑的记忆面板，覆盖记忆库、角色状态、世界事实和修订笔记。 |
| Workspace Tools | Planning, sync, retrieval, revision, and chapter operations in one place. | 在一个界面中完成规划、同步、检索、修订和章节操作。 |

## Interface Preview | 界面预览

These screenshots show the current Write-Claw interface in action.  
下面这些截图展示了当前 Write-Claw 的实际界面效果。

### Runtime Flow | 运行流程

<table>
  <tr>
    <td width="33%">
      <img src="png/1.png" alt="Write-Claw UI Preview 01" />
      <p align="center"><sub>Live runtime trace / 实时运行轨迹</sub></p>
    </td>
    <td width="33%">
      <img src="png/2.png" alt="Write-Claw UI Preview 02" />
      <p align="center"><sub>Main chat surface / 主对话界面</sub></p>
    </td>
    <td width="33%">
      <img src="png/3.png" alt="Write-Claw UI Preview 03" />
      <p align="center"><sub>Chapter progress flow / 章节推进流程</sub></p>
    </td>
  </tr>
</table>

### Workspace and Assets | 工作区与资产

<table>
  <tr>
    <td width="33%">
      <img src="png/4.png" alt="Write-Claw UI Preview 04" />
      <p align="center"><sub>Character archive / 角色档案</sub></p>
    </td>
    <td width="33%">
      <img src="png/5.png" alt="Write-Claw UI Preview 05" />
      <p align="center"><sub>World and context view / 世界与上下文视图</sub></p>
    </td>
    <td width="33%">
      <img src="png/6.png" alt="Write-Claw UI Preview 06" />
      <p align="center"><sub>Storyboard workspace / 故事板工作区</sub></p>
    </td>
  </tr>
</table>

### Memory and Editing | 记忆与编辑

<table>
  <tr>
    <td width="33%">
      <img src="png/7.png" alt="Write-Claw UI Preview 07" />
      <p align="center"><sub>Memory overview / 记忆总览</sub></p>
    </td>
    <td width="33%">
      <img src="png/8.png" alt="Write-Claw UI Preview 08" />
      <p align="center"><sub>Editable workspace detail / 可编辑工作区详情</sub></p>
    </td>
    <td width="33%">
      <img src="png/9.png" alt="Write-Claw UI Preview 09" />
      <p align="center"><sub>Capability control / 能力控制台</sub></p>
    </td>
  </tr>
</table>

### Models, Sessions, and System Views | 模型、会话与系统视图

<table>
  <tr>
    <td width="33%">
      <img src="png/10.png" alt="Write-Claw UI Preview 10" />
      <p align="center"><sub>Model settings / 模型配置</sub></p>
    </td>
    <td width="33%">
      <img src="png/11.png" alt="Write-Claw UI Preview 11" />
      <p align="center"><sub>Session center / 会话中心</sub></p>
    </td>
    <td width="33%">
      <img src="png/12.png" alt="Write-Claw UI Preview 12" />
      <p align="center"><sub>Status and trace / 状态与轨迹</sub></p>
    </td>
  </tr>
</table>

### Extended Views | 扩展视图

<table>
  <tr>
    <td width="33%">
      <img src="png/13.png" alt="Write-Claw UI Preview 13" />
      <p align="center"><sub>Skills and agents / 技能与代理</sub></p>
    </td>
    <td width="33%">
      <img src="png/14.png" alt="Write-Claw UI Preview 14" />
      <p align="center"><sub>Writing workspace / 写作工作台</sub></p>
    </td>
    <td width="33%">
      <img src="png/15.png" alt="Write-Claw UI Preview 15" />
      <p align="center"><sub>System capability stack / 系统能力栈</sub></p>
    </td>
  </tr>
</table>

## Who Is This For | 适合谁

Write-Claw is especially interesting for:

- writers who want chapter-level control instead of one-shot generation
- developers exploring agents, memory systems, tools, and runtime interaction
- researchers interested in long-form writing, orchestration, and human-in-the-loop systems

<a id="installation"></a>

## Installation | 安装与启动

### 1. Run locally | 本地启动

```powershell
cd Write-Claw
.\local_web_portal\start_local.ps1
```

Open in browser:

```text
http://127.0.0.1:8010
```

### 2. Prepare environment | 准备环境变量

```powershell
Copy-Item local_web_portal\.env.example local_web_portal\.env
```

Fill in your own provider keys and local settings.  
Do **not** commit `local_web_portal\.env`.

<a id="integrations"></a>

## Integrations | Claude 与 Codex 插件包

This repository now also includes two host-specific packaging modes for reuse:

- `integrations/claude-plugin-bundle`
  A Claude-oriented plugin package using a `.claude-plugin` layout.
- `integrations/codex-skill-bundle`
  A Codex-oriented skill package using `AGENTS.md` and `.codex/skills`.

These packaging modes are meant for distribution and reuse.  
They do **not** make MCP mandatory.

Use the host package directly when you mainly need:

- workflow prompts
- writing agents or skills
- reusable templates
- host-specific installation structure

Add MCP later only if you want a shared tool-calling layer for runtime control, memory access, or chapter synchronization.

<a id="plugin-usage"></a>

## Plugin Usage | 插件使用方法

### Claude plugin bundle

1. Download `write-claw-claude-plugin.zip` from Releases or use `integrations/claude-plugin-bundle`.
2. Unzip it into the repository or workspace where you want Claude-compatible plugin assets.
3. Keep the `.claude-plugin` directory structure unchanged.
4. Start with the plugin entry and `prompts/session-kickoff.md` to initialize a new writing project.
5. Use the bundled agents and skill for chapter planning, memory maintenance, and revision flow.

### Codex skill bundle

1. Download `write-claw-codex-skill.zip` from Releases or use `integrations/codex-skill-bundle`.
2. Copy `AGENTS.md`, `.codex/skills/write-claw-runtime`, and `templates/` into the target repository.
3. Let Codex read the workspace `AGENTS.md` so the `write-claw-runtime` skill becomes available.
4. Use the provided templates to build a story brief, chapter checkpoint, and memory notes before drafting.
5. Keep canon updates and continuity fixes explicit between chapters.

### Do you need MCP

No. MCP is optional here.

Use these bundles directly when you mainly need:

- reusable prompts
- host-specific plugin or skill structure
- chapter workflow guidance
- memory and continuity conventions

Add MCP later only if you need standard tool calls for runtime control, memory access, or chapter synchronization.

<a id="releases"></a>

## Releases | Release 打包

Prepacked release artifacts for the two plugin modes are available in:

- `release/write-claw-claude-plugin.zip`
- `release/write-claw-codex-skill.zip`

If you want to publish GitHub Releases later, these two zip files are the recommended upload assets.

<a id="repository-layout"></a>

## Repository Layout

```text
Write-Claw/
├─ agents/                # agent implementations
├─ rag/                   # memory and retrieval
├─ utils/                 # shared helpers
├─ workflow/              # orchestration and execution
├─ local_web_portal/
│  ├─ app/                # FastAPI web application
│  ├─ start_local.ps1     # local startup script
│  └─ .env.example        # environment template
├─ integrations/          # Claude / Codex reusable packages
├─ release/               # packaged release zip assets
├─ png/                   # README screenshots
├─ main.py
├─ config.py
├─ capability_registry.py
└─ requirements.txt
```

## Project Role | 项目定位

You can understand this repository as:

- a standalone runtime repo for the Write-Claw experience
- a visual project surface for showing how Claw can work in writing
- a foundation for future work on MCP, skills, memory, and long-form agentic creation
