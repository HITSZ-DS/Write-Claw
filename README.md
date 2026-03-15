# Write-Claw

<div align="center">

**Claw-native long-form writing workspace**  
**面向长篇创作的 Claw 原生写作工作台**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Portal-009688?style=flat-square&logo=fastapi&logoColor=white)
![Mode](https://img.shields.io/badge/Mode-Write--Claw-111827?style=flat-square)
![Runtime](https://img.shields.io/badge/Runtime-Live%20Trace-2563EB?style=flat-square)
![Language](https://img.shields.io/badge/Language-中文%20%2F%20English-7C3AED?style=flat-square)

</div>

---

## Overview | 项目简介

`Write-Claw` is a clean, GitHub-ready runtime package focused on the actual Claw writing experience: live orchestration, editable memory, workspace views, chapter checkpoints, and an integrated local web portal.  
`Write-Claw` 是一个面向 GitHub 整理后的干净运行包，核心聚焦在真正的 Claw 写作体验上：实时调度、可编辑记忆、工作区视图、章节 checkpoint，以及一体化的本地 Web 门户。

Instead of presenting a static shell around a fixed workflow, this repository pushes toward a more interactive writing system where the runtime can think, pause, ask, revise, sync, and continue inside one continuous workspace.  
它不是套在固定流程外面的静态壳，而是朝着更真实的交互式写作系统推进：运行时可以在一个连续工作区里思考、暂停、提问、修订、同步并继续创作。

## Why Write-Claw | 为什么是 Write-Claw

- `Claw-native orchestration`
  The writing loop is no longer hidden behind a rigid pipeline.
  `Claw 原生调度`
  写作循环不再被隐藏在僵硬的固定流程后面。

- `Live runtime interaction`
  Mid-run questions, checkpoints, and interrupts stay on the same page.
  `实时运行交互`
  运行中提问、章节检查点和中途打断都留在同一页完成。

- `Editable memory and workspace`
  Character cards, world facts, planning packets, and chapter assets are visible and operable.
  `可编辑记忆与工作区`
  角色卡、世界事实、规划包和章节资产都可以直接查看和操作。

- `GitHub-clean package`
  This repo is suitable as a standalone shareable runtime surface.
  `干净的 GitHub 包`
  这个仓库适合作为独立、可共享的运行时项目表面。

## Core Experience | 核心体验

| Module | English | 中文 |
| --- | --- | --- |
| Runtime Loop | Dynamic Claw loop with live tool trace, chapter decisions, and visible execution flow. | 动态 Claw 循环，提供实时工具轨迹、章节决策和可见执行流程。 |
| Writing Console | A multi-view console for chat, run progress, checkpoints, and manuscript work. | 多视图写作控制台，整合对话、运行进度、checkpoint 和稿件工作区。 |
| Memory Surface | Bilingual panels for memory banks, world state, character state, and revision notes. | 双语记忆面板，覆盖记忆库、世界状态、角色状态与修订笔记。 |
| Workspace Tools | Planning, sync, retrieval, revision, and manuscript operations in one surface. | 在统一界面中完成规划、同步、检索、修订和稿件操作。 |

## Interface Preview | 界面预览

Below is a screenshot gallery from the current Write-Claw interface.  
下面是当前 Write-Claw 界面的截图画廊。

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

### Extended Console Views | 扩展控制台视图

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

## Clean Package Notes | 干净包说明

This repository is intentionally kept cleaner than the original working directory.  
这个仓库是按“比原始工作目录更干净”的标准整理的。

Excluded from versioned runtime state:
- Local databases
- Generated runs and logs
- Vector store data
- Session secrets and encryption keys
- Virtual environments and caches

被排除在版本化运行状态之外的内容包括：
- 本地数据库
- 运行产物与日志
- 向量库存储数据
- 会话密钥与加密密钥
- 虚拟环境与缓存

## Positioning | 仓库定位

Use this repository as:
- A standalone runtime repo for Write-Claw
- A cleaner deployment surface for local or private hosting
- A shareable bilingual project page for the Claw writing experience

你可以把这个仓库当作：
- Write-Claw 的独立运行仓库
- 更干净的本地或私有部署表面
- 一个可展示 Claw 写作体验的双语项目主页
