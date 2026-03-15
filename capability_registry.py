from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Set


@dataclass(frozen=True)
class CapabilitySpec:
    slug: str
    name_en: str
    name_zh: str
    category_en: str
    category_zh: str
    description_en: str
    description_zh: str
    manager_action: Optional[str] = None
    default_enabled: bool = True
    always_enabled: bool = False
    order: int = 0


CAPABILITY_REGISTRY: List[CapabilitySpec] = [
    CapabilitySpec(
        slug="plot_strategy",
        name_en="Plot Strategy",
        name_zh="情节策略",
        category_en="Claw Actions",
        category_zh="Claw 动作",
        description_en="Plan chapter progression, conflict escalation, and turning beats before drafting.",
        description_zh="在起草正文前规划章节推进、冲突升级与关键转折点。",
        manager_action="plot_strategy",
        order=10,
    ),
    CapabilitySpec(
        slug="retrieve_context",
        name_en="Context Retrieval",
        name_zh="上下文检索",
        category_en="Claw Actions",
        category_zh="Claw 动作",
        description_en="Pull relevant dynamic-memory context, facts, and recent writing state back into the loop.",
        description_zh="把相关的动态记忆、事实信息和最近写作状态重新拉回当前循环。",
        manager_action="retrieve_context",
        order=20,
    ),
    CapabilitySpec(
        slug="enrich_character",
        name_en="Character Enrichment",
        name_zh="人物强化",
        category_en="Claw Actions",
        category_zh="Claw 动作",
        description_en="Strengthen motives, relationships, behavioral boundaries, and character consistency.",
        description_zh="强化人物动机、关系网络、行为边界和角色一致性。",
        manager_action="enrich_character",
        order=30,
    ),
    CapabilitySpec(
        slug="enrich_world",
        name_en="World Enrichment",
        name_zh="世界观强化",
        category_en="Claw Actions",
        category_zh="Claw 动作",
        description_en="Clarify world rules, scene constraints, setting facts, and reusable canon.",
        description_zh="明确世界规则、场景约束、设定事实和可复用的正典信息。",
        manager_action="enrich_world",
        order=40,
    ),
    CapabilitySpec(
        slug="inspect_workspace",
        name_en="Inspect Workspace",
        name_zh="检查工作区",
        category_en="Local Tools",
        category_zh="本地工具",
        description_en="Inspect the local run workspace, chapter files, and current memory assets before acting.",
        description_zh="在执行下一步之前，检查本地运行工作区、章节文件和当前记忆资产。",
        manager_action="inspect_workspace",
        order=45,
    ),
    CapabilitySpec(
        slug="draft_chapter",
        name_en="Draft Chapter",
        name_zh="章节起草",
        category_en="Core Writing",
        category_zh="核心写作",
        description_en="Generate the main prose draft for the current chapter.",
        description_zh="生成当前章节的主体正文草稿。",
        manager_action="draft_chapter",
        always_enabled=True,
        order=50,
    ),
    CapabilitySpec(
        slug="rewrite_chapter",
        name_en="Rewrite Chapter",
        name_zh="章节重写",
        category_en="Core Writing",
        category_zh="核心写作",
        description_en="Rewrite or compress drafts when quality, pacing, or length misses the target.",
        description_zh="当质量、节奏或长度不达标时，对草稿进行重写或压缩。",
        manager_action="rewrite_chapter",
        always_enabled=True,
        order=60,
    ),
    CapabilitySpec(
        slug="finalize",
        name_en="Finalize",
        name_zh="定稿",
        category_en="Core Writing",
        category_zh="核心写作",
        description_en="Finalize the chapter once the current candidate is acceptable.",
        description_zh="当当前候选稿达到可接受标准后完成定稿。",
        manager_action="finalize",
        always_enabled=True,
        order=70,
    ),
    CapabilitySpec(
        slug="sync_storyboard",
        name_en="Sync Storyboard",
        name_zh="同步故事板",
        category_en="Local Tools",
        category_zh="本地工具",
        description_en="Write the current chapter brief and Claw plan into local workspace files and outline assets.",
        description_zh="把当前章节 brief 和 Claw 计划写入本地工作区文件与大纲资产。",
        manager_action="sync_storyboard",
        order=80,
    ),
    CapabilitySpec(
        slug="sync_characters",
        name_en="Sync Characters",
        name_zh="同步角色资产",
        category_en="Local Tools",
        category_zh="本地工具",
        description_en="Extract current character state and write it into local files plus character memory.",
        description_zh="提取当前角色状态，并写入本地文件以及角色记忆。",
        manager_action="sync_characters",
        order=90,
    ),
    CapabilitySpec(
        slug="sync_world",
        name_en="Sync World",
        name_zh="同步世界设定",
        category_en="Local Tools",
        category_zh="本地工具",
        description_en="Extract world rules and continuity facts into local workspace files and world memory.",
        description_zh="把世界规则与连续性事实提取到本地工作区文件和世界记忆。",
        manager_action="sync_world",
        order=100,
    ),
    CapabilitySpec(
        slug="idea_analyzer",
        name_en="Idea Analyzer",
        name_zh="创意分析",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Turn a rough idea into a stable brief with genre, cast, goals, and constraints.",
        description_zh="把粗糙想法整理为包含题材、角色、目标和约束的稳定提案。",
        order=110,
    ),
    CapabilitySpec(
        slug="analyzer",
        name_en="Task Analyzer",
        name_zh="任务分析",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Understand whether the current step needs planning, drafting, revision, or cleanup.",
        description_zh="判断当前步骤更需要规划、起草、修订还是收束整理。",
        order=120,
    ),
    CapabilitySpec(
        slug="dynamic_memory",
        name_en="Dynamic Memory",
        name_zh="动态记忆",
        category_en="Memory System",
        category_zh="记忆系统",
        description_en="Persist reusable story state, chapter briefs, facts, and working memory across iterations.",
        description_zh="跨轮次保存可复用的故事状态、章节简报、事实信息和工作记忆。",
        always_enabled=True,
        order=130,
    ),
    CapabilitySpec(
        slug="turning_point_tracker",
        name_en="Turning Point Tracker",
        name_zh="转折点追踪",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Track whether chapters are meaningfully advancing the story.",
        description_zh="追踪章节是否在真正推动故事向前发展。",
        order=140,
    ),
    CapabilitySpec(
        slug="consistency_checker",
        name_en="Consistency Checker",
        name_zh="一致性检查",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Check continuity across character, world, timeline, and established facts.",
        description_zh="检查人物、世界观、时间线和既有事实之间的连续性。",
        order=150,
    ),
    CapabilitySpec(
        slug="realtime_editor",
        name_en="Realtime Editor",
        name_zh="实时编辑",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Find weak spans in a draft and apply targeted revision passes.",
        description_zh="定位草稿中的薄弱片段并执行针对性的修订。",
        order=160,
    ),
    CapabilitySpec(
        slug="evaluator",
        name_en="Evaluator",
        name_zh="评估器",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Score coherence, pacing, emotional impact, and task fit of candidate drafts.",
        description_zh="评估候选稿的一致性、节奏、情绪力度和任务匹配度。",
        order=170,
    ),
    CapabilitySpec(
        slug="judge",
        name_en="Judge",
        name_zh="裁决器",
        category_en="Support Skills",
        category_zh="辅助技能",
        description_en="Break ties between close chapter candidates when rewards are too similar.",
        description_zh="当多个章节候选结果接近时，用于做最终裁决。",
        order=180,
    ),
]


def capability_map() -> Dict[str, CapabilitySpec]:
    return {item.slug: item for item in CAPABILITY_REGISTRY}


def default_enabled_capability_slugs() -> Set[str]:
    return {item.slug for item in CAPABILITY_REGISTRY if item.default_enabled or item.always_enabled}


def normalize_capability_slugs(values: Iterable[str]) -> Set[str]:
    known = capability_map()
    out: Set[str] = set()
    for value in values:
        slug = str(value or "").strip().lower()
        if slug in known:
            out.add(slug)
    for item in CAPABILITY_REGISTRY:
        if item.always_enabled:
            out.add(item.slug)
    return out


def enabled_capability_slugs_from_env(raw: str) -> Set[str]:
    text = str(raw or "").strip()
    if not text:
        return default_enabled_capability_slugs()
    return normalize_capability_slugs(text.split(","))


def claw_action_specs() -> List[CapabilitySpec]:
    return [item for item in CAPABILITY_REGISTRY if item.manager_action]


def enabled_claw_actions(enabled_slugs: Iterable[str]) -> Set[str]:
    enabled = normalize_capability_slugs(enabled_slugs)
    actions: Set[str] = set()
    for item in claw_action_specs():
        if item.always_enabled or item.slug in enabled:
            actions.add(str(item.manager_action))
    return actions
