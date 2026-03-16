# Write-Claw

<div align="center">

**A claw-native workspace for long-form AI writing**  
**一个面向长篇 AI 写作的 Claw 原生工作台**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Portal-009688?style=flat-square&logo=fastapi&logoColor=white)
![Runtime](https://img.shields.io/badge/Runtime-Live%20Trace-2563EB?style=flat-square)
![Interaction](https://img.shields.io/badge/Interaction-Checkpoint%20%26%20Interrupt-7C3AED?style=flat-square)
![Language](https://img.shields.io/badge/Language-中文%20%2F%20English-111827?style=flat-square)

</div>

---

## Opening | 开场一句

Write-Claw is built around a simple idea:  
AI writing should not stop at “prompt in, text out.”

Write-Claw 围绕一个很直接的目标展开：  
AI 写作不该停留在“输入一句，生成一段”。

It should be able to plan, write, pause, revise, remember, and keep the author inside the loop.  
它应该能够规划、写作、暂停、修订、记忆，并且始终把作者保留在创作循环里。

## Overview | 项目简介

`Write-Claw` is a runtime-focused writing workspace for long-form creation.  
It combines a local web portal, a Claw-style orchestration loop, editable memory surfaces, chapter checkpoints, and a visible execution trace into one continuous workflow.

`Write-Claw` 是一个面向长篇创作的运行时写作工作台。  
它把本地 Web 门户、Claw 风格调度循环、可编辑记忆面板、章节 checkpoint 和可见执行轨迹整合到同一个连续工作流中。

## Why It Gets Attention | 为什么它更容易吸引人

Most writing tools show only the output.  
Write-Claw tries to show the process.

大多数写作工具只展示结果。  
Write-Claw 更想把“过程”本身做出来。

- `Visible runtime`
  You can see what the system is doing, instead of trusting a black box.
  `可见运行时`
  你可以看到系统正在做什么，而不是只能相信一个黑箱。

- `Interruptible flow`
  You can stop, steer, and adjust direction while the writing is still happening.
  `可打断流程`
  你可以在写作进行中随时打断、改向、继续推进。

- `Checkpoint-driven chapters`
  Each chapter can become a decision point, not just a generated artifact.
  `章节式 checkpoint`
  每一章都可以成为一个决策节点，而不只是生成产物。

- `Memory-first collaboration`
  Character state, world state, notes, and planning can accumulate over time.
  `记忆优先的协作写作`
  角色状态、世界状态、笔记与规划会在写作过程中持续积累。

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

### Workspace & Assets | 工作区与资产

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

### Memory & Editing | 记忆与编辑

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

## Who Is This For | 这适合谁

Write-Claw is especially interesting for:

- writers who want chapter-level control instead of one-shot generation  
  想要章节级控制，而不是一次性生成的作者
- developers exploring agents, memory systems, tools, and runtime interaction  
  正在探索 agent、记忆系统、工具调用和运行时交互的开发者
- researchers interested in long-form writing, orchestration, and human-in-the-loop systems  
  关注长文本写作、任务编排和 human-in-the-loop 系统的研究者

## Quick Start | 快速开始

### 1. Run locally | 本地启动

```powershell
cd Write-Claw
.\local_web_portal\start_local.ps1
```

Open in browser:  
浏览器访问：

```text
http://127.0.0.1:8010
```

### 2. Prepare environment | 准备环境变量

```powershell
Copy-Item local_web_portal\.env.example local_web_portal\.env
```

Fill in your own provider keys and local settings.  
填写你自己的 provider 密钥和本地配置。

Do **not** commit `local_web_portal\.env`.  
不要提交 `local_web_portal\.env`。

## Repository Layout | 仓库结构

```text
Write-Claw/
├─ agents/                # agent implementations | Agent 实现
├─ rag/                   # memory and retrieval | 记忆与检索
├─ utils/                 # shared helpers | 通用工具
├─ workflow/              # orchestration and execution | 编排与执行
├─ local_web_portal/
│  ├─ app/                # FastAPI web application | Web 应用
│  ├─ start_local.ps1     # local startup script | 本地启动脚本
│  └─ .env.example        # environment template | 环境模板
├─ png/                   # README screenshots | README 截图资源
├─ main.py
├─ config.py
├─ capability_registry.py
└─ requirements.txt
```

## Project Role | 项目定位

You can understand this repository as:

- a standalone runtime repo for the Write-Claw experience  
  一个可独立运行的 Write-Claw 仓库
- a visual project surface for showing how Claw can work in writing  
  一个展示 Claw 如何进入写作场景的项目表面
- a foundation for future work on MCP, skills, memory, and long-form agentic creation  
  一个继续拓展 MCP、skills、记忆系统和长篇 agent 创作的基础项目
