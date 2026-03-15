from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from config import Config
from utils.language_detector import detect_language
from utils.llm_client import LLMClient


@dataclass(frozen=True)
class ProviderRuntime:
    slug: str
    base_url: str
    model: str
    wire_api: str = "chat"


class IdeaCopilotAgent:
    """Language-routed collaborative ideation agent for WriteClaw."""

    def __init__(self, provider_spec: Any, api_key: str):
        self.provider = _to_provider_runtime(provider_spec)
        self.api_key = api_key

    def generate_turn(
        self,
        *,
        original_idea: str,
        state: Dict[str, Any],
        latest_user_reply: str,
    ) -> Dict[str, Any]:
        return generate_assistant_turn(
            original_idea=original_idea,
            state=state,
            latest_user_reply=latest_user_reply,
            provider_spec=self.provider,
            api_key=self.api_key,
        )

    @staticmethod
    def load_state(raw: str) -> Dict[str, Any]:
        return load_state(raw)

    @staticmethod
    def dump_state(state: Dict[str, Any]) -> str:
        return dump_state(state)

    @staticmethod
    def append_user(state: Dict[str, Any], reply: str) -> Dict[str, Any]:
        return append_user_reply(state, reply)

    @staticmethod
    def append_assistant(state: Dict[str, Any], turn: Dict[str, Any]) -> Dict[str, Any]:
        return append_assistant_turn(state, turn)

    @staticmethod
    def latest_turn(state: Dict[str, Any]) -> Dict[str, Any]:
        return latest_assistant_turn(state)

    @staticmethod
    def to_generation_idea(original_idea: str, state: Dict[str, Any]) -> str:
        return build_generation_idea(original_idea, state)


GENERATION_SCOPES = {"auto", "all", "limited", "chapter_by_chapter"}
CHAPTER_PAUSE_MODES = {"manual_each_chapter", "run_to_end", "auto"}


def default_generation_preferences() -> Dict[str, Any]:
    return {
        "generation_scope": "auto",
        "requested_chapters": 0,
        "chapter_pause_mode": "manual_each_chapter",
        "user_request": "",
    }


def normalize_generation_preferences(value: Any) -> Dict[str, Any]:
    out = dict(default_generation_preferences())
    if isinstance(value, dict):
        scope = str(value.get("generation_scope") or out["generation_scope"]).strip().lower()
        if scope in GENERATION_SCOPES:
            out["generation_scope"] = scope
        pause_mode = str(value.get("chapter_pause_mode") or out["chapter_pause_mode"]).strip().lower()
        if pause_mode in CHAPTER_PAUSE_MODES:
            out["chapter_pause_mode"] = pause_mode
        try:
            requested = max(0, int(value.get("requested_chapters") or 0))
        except Exception:
            requested = 0
        out["requested_chapters"] = requested
        out["user_request"] = str(value.get("user_request") or "").strip()[:400]

    if out["generation_scope"] == "limited" and out["requested_chapters"] <= 0:
        out["requested_chapters"] = 1
    if out["generation_scope"] == "all":
        out["requested_chapters"] = 0
    if out["generation_scope"] == "chapter_by_chapter":
        out["chapter_pause_mode"] = "manual_each_chapter"
    if out["chapter_pause_mode"] == "auto":
        out["chapter_pause_mode"] = (
            "run_to_end" if out["generation_scope"] in {"all", "limited"} else "manual_each_chapter"
        )
    return out


def merge_generation_preferences(state: Dict[str, Any], updates: Any) -> Dict[str, Any]:
    merged = normalize_generation_preferences(state.get("generation_preferences"))
    if isinstance(updates, dict):
        candidate = dict(merged)
        for key in ("generation_scope", "requested_chapters", "chapter_pause_mode", "user_request"):
            if key in updates and updates.get(key) not in {None, ""}:
                candidate[key] = updates.get(key)
        merged = normalize_generation_preferences(candidate)
    return merged


def _to_provider_runtime(spec: Any) -> ProviderRuntime:
    if isinstance(spec, ProviderRuntime):
        return spec
    if isinstance(spec, dict):
        return ProviderRuntime(
            slug=str(spec.get("slug") or ""),
            base_url=str(spec.get("base_url") or ""),
            model=str(spec.get("model") or ""),
            wire_api=str(spec.get("wire_api") or "chat"),
        )
    return ProviderRuntime(
        slug=str(getattr(spec, "slug", "") or ""),
        base_url=str(getattr(spec, "base_url", "") or ""),
        model=str(getattr(spec, "model", "") or ""),
        wire_api=str(getattr(spec, "wire_api", "chat") or "chat"),
    )


def load_state(raw: str) -> Dict[str, Any]:
    base: Dict[str, Any] = {
        "version": 3,
        "messages": [],
        "refined_idea": "",
        "round": 0,
        "preferred_language": "en",
        "source_language": "en",
        "ui_language": "en",
        "translation_mode": "follow_input",
        "generation_preferences": default_generation_preferences(),
        "reply_pending": False,
        "reply_error": "",
        "reply_started_at": "",
    }
    if not raw:
        return base
    try:
        data = json.loads(raw)
    except Exception:
        return base
    if not isinstance(data, dict):
        return base
    out = dict(base)
    msgs = data.get("messages")
    if isinstance(msgs, list):
        out["messages"] = msgs
    out["refined_idea"] = str(data.get("refined_idea") or "")
    out["preferred_language"] = str(data.get("preferred_language") or "en").lower()
    out["source_language"] = str(data.get("source_language") or out["preferred_language"] or "en").lower()
    out["ui_language"] = str(data.get("ui_language") or "en").lower()
    out["translation_mode"] = str(data.get("translation_mode") or "follow_input")
    out["generation_preferences"] = normalize_generation_preferences(data.get("generation_preferences"))
    out["reply_pending"] = bool(data.get("reply_pending") or False)
    out["reply_error"] = str(data.get("reply_error") or "")
    out["reply_started_at"] = str(data.get("reply_started_at") or "")
    try:
        out["round"] = max(0, int(data.get("round") or 0))
    except Exception:
        out["round"] = 0
    return out


def dump_state(state: Dict[str, Any]) -> str:
    payload = {
        "version": 3,
        "messages": state.get("messages", []),
        "refined_idea": state.get("refined_idea", ""),
        "round": int(state.get("round", 0) or 0),
        "preferred_language": state.get("preferred_language", "en"),
        "source_language": state.get("source_language", state.get("preferred_language", "en")),
        "ui_language": state.get("ui_language", "en"),
        "translation_mode": state.get("translation_mode", "follow_input"),
        "generation_preferences": normalize_generation_preferences(state.get("generation_preferences")),
        "reply_pending": bool(state.get("reply_pending") or False),
        "reply_error": str(state.get("reply_error") or ""),
        "reply_started_at": str(state.get("reply_started_at") or ""),
    }
    return json.dumps(payload, ensure_ascii=False)


def _build_client(spec: ProviderRuntime, api_key: str, preferred_language: str) -> LLMClient:
    cfg = Config(require_api_key=False)
    cfg.language = preferred_language if preferred_language in {"en", "zh"} else "en"
    cfg.llm_provider = spec.slug
    cfg.api_key = api_key
    cfg.api_base_url = spec.base_url
    cfg.model_name = spec.model
    cfg.wire_api = spec.wire_api
    cfg.temperature = 0.6
    cfg.max_tokens = min(int(getattr(cfg, "max_tokens", 1600) or 1600), 1600)
    return LLMClient(cfg)


def _extract_json_object(text: str) -> Optional[str]:
    s = (text or "").strip()
    if not s:
        return None
    start = s.find("{")
    if start < 0:
        return None
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(s)):
        ch = s[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return s[start : i + 1]
    return None


def _history_text(messages: List[Dict[str, Any]], limit: int = 12) -> str:
    if not messages:
        return "(no prior conversation yet)"
    rows: List[str] = []
    for item in messages[-limit:]:
        role = str(item.get("role") or "").strip().lower()
        if role == "assistant":
            analysis = str(item.get("analysis") or "").strip()
            refined = str(item.get("refined_idea") or "").strip()
            questions = item.get("questions") or []
            row = f"assistant analysis: {analysis[:300]}"
            if refined:
                row += f" | brief: {refined[:300]}"
            if isinstance(questions, list) and questions:
                row += " | questions: " + " ; ".join(str(q)[:120] for q in questions[:3])
            rows.append(row)
        elif role == "user":
            rows.append(f"user: {str(item.get('content') or '').strip()[:400]}")
    return "\n".join(rows) if rows else "(no prior conversation yet)"


def _normalize_questions(value: Any) -> List[str]:
    if isinstance(value, list):
        out = []
        for item in value[:3]:
            text = str(item or "").strip()
            if text:
                out.append(text[:200])
        return out
    if isinstance(value, str) and value.strip():
        return [value.strip()[:200]]
    return []


def _normalize_turn(parsed: Dict[str, Any], fallback_refined: str, fallback_text: str, preferred_language: str) -> Dict[str, Any]:
    refined = str(parsed.get("refined_idea") or fallback_refined or "").strip()
    analysis = str(
        parsed.get("analysis")
        or fallback_text
        or (
            "Please refine the premise, constraints, and intended output."
            if preferred_language == "en"
            else "请进一步明确故事前提、限制条件和预期输出。"
        )
    ).strip()
    questions = _normalize_questions(parsed.get("questions"))
    try:
        readiness = max(0, min(100, int(parsed.get("readiness") or 0)))
    except Exception:
        readiness = 0
    ready_hint = str(
        parsed.get("ready_hint")
        or (
            "Keep clarifying the premise, world rules, character arcs, and style goals."
            if preferred_language == "en"
            else "请继续补充故事前提、世界规则、人物弧线和风格目标。"
        )
    ).strip()
    language = str(parsed.get("language") or preferred_language or "en").lower()
    style_targets = _normalize_questions(parsed.get("style_targets"))
    memory_targets = _normalize_questions(parsed.get("memory_targets"))
    return {
        "role": "assistant",
        "analysis": analysis[:2400],
        "refined_idea": refined[:5000],
        "questions": questions,
        "readiness": readiness,
        "ready_hint": ready_hint[:600],
        "language": language if language in {"en", "zh"} else preferred_language,
        "style_targets": style_targets,
        "memory_targets": memory_targets,
    }


def _fallback_turn(state: Dict[str, Any], original_idea: str, raw_response: str) -> Dict[str, Any]:
    preferred_language = str(state.get("preferred_language") or "en").lower()
    fallback_refined = str(state.get("refined_idea") or "").strip() or original_idea.strip()
    return _normalize_turn(
        parsed={},
        fallback_refined=fallback_refined,
        fallback_text=raw_response or (
            "I need a bit more detail about the story, style, and constraints before moving forward."
            if preferred_language == "en"
            else "在继续之前，我还需要更多关于故事、风格和硬性约束的细节。"
        ),
        preferred_language=preferred_language,
    )


def generate_assistant_turn(
    *,
    original_idea: str,
    state: Dict[str, Any],
    latest_user_reply: str,
    provider_spec: Any,
    api_key: str,
) -> Dict[str, Any]:
    runtime = _to_provider_runtime(provider_spec)
    preferred_language = str(state.get("preferred_language") or "en").lower()
    source_language = str(state.get("source_language") or detect_language(original_idea)).lower()
    client = _build_client(runtime, api_key, preferred_language)
    current_refined = str(state.get("refined_idea") or "").strip() or original_idea.strip()
    history = _history_text(state.get("messages") or [])

    output_lang = "English" if preferred_language == "en" else "Chinese"
    system_prompt = f"""You are WriteClaw's collaborative ideation agent.
Goal: turn a raw story idea into a stable writing brief that can drive a real agentic writing loop.
Rules:
1) Ask at most 3 high-value questions each turn.
2) First provide analysis, then a refined brief, then targeted questions.
3) Focus on conflict, cast, world rules, voice, structure, and hard constraints.
4) If the user clearly asks to start writing or generation, prepare the brief for execution instead of forcing more refinement.
5) Output strict JSON only, in {output_lang}.
JSON schema:
{{
  "analysis": "string",
  "refined_idea": "string",
  "questions": ["q1", "q2"],
  "readiness": 0,
  "ready_hint": "string",
  "language": "en",
  "style_targets": ["voice or tone target"],
  "memory_targets": ["memory item that should be remembered"]
}}
"""

    user_prompt = f"""[original idea]
{original_idea}

[current brief]
{current_refined}

[user reply this turn]
{latest_user_reply or '(first turn, no user reply yet)'}

[source language]
{source_language}

[target language]
{preferred_language}

[recent conversation]
{history}

Produce the next ideation turn now.
"""

    raw = client.chat(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.6,
        max_tokens=1400,
    )

    block = _extract_json_object(raw or "")
    if not block:
        return _fallback_turn(state, original_idea, raw or "")
    try:
        parsed = json.loads(block)
    except Exception:
        return _fallback_turn(state, original_idea, raw or "")
    if not isinstance(parsed, dict):
        return _fallback_turn(state, original_idea, raw or "")
    return _normalize_turn(
        parsed=parsed,
        fallback_refined=current_refined,
        fallback_text=raw or "",
        preferred_language=preferred_language,
    )


def append_user_reply(state: Dict[str, Any], reply: str) -> Dict[str, Any]:
    content = (reply or "").strip()
    if not content:
        return state
    out = load_state(dump_state(state))
    msgs = list(out.get("messages") or [])
    msgs.append({"role": "user", "content": content[:3000]})
    out["messages"] = msgs[-30:]
    detected = detect_language(content)
    if detected in {"en", "zh"}:
        out["preferred_language"] = detected
        out["source_language"] = detected
    return out


def append_assistant_turn(state: Dict[str, Any], turn: Dict[str, Any]) -> Dict[str, Any]:
    out = load_state(dump_state(state))
    msgs = list(out.get("messages") or [])
    msgs.append(turn)
    out["messages"] = msgs[-30:]
    out["refined_idea"] = str(turn.get("refined_idea") or out.get("refined_idea") or "")
    out["round"] = int(out.get("round", 0) or 0) + 1
    turn_lang = str(turn.get("language") or "").lower()
    if turn_lang in {"en", "zh"}:
        out["preferred_language"] = turn_lang
    return out


def latest_assistant_turn(state: Dict[str, Any]) -> Dict[str, Any]:
    msgs = list(state.get("messages") or [])
    for item in reversed(msgs):
        if str(item.get("role") or "") == "assistant":
            return item
    return {
        "role": "assistant",
        "analysis": (
            "Start a writing session and I will refine the idea into a stronger writing brief."
            if str(state.get("preferred_language") or "en").lower() == "en"
            else "开始一个写作会话后，我会把你的想法打磨成更稳定、更可执行的写作 brief。"
        ),
        "refined_idea": state.get("refined_idea") or "",
        "questions": [],
        "readiness": 0,
        "ready_hint": "",
        "language": str(state.get("preferred_language") or "en"),
        "style_targets": [],
        "memory_targets": [],
    }


def build_generation_idea(original_idea: str, state: Dict[str, Any]) -> str:
    refined = str(state.get("refined_idea") or "").strip() or original_idea.strip()
    messages = list(state.get("messages") or [])
    generation_preferences = normalize_generation_preferences(state.get("generation_preferences"))
    qa: List[str] = []
    style_targets: List[str] = []
    memory_targets: List[str] = []
    for item in messages[-20:]:
        role = str(item.get("role") or "")
        if role == "assistant":
            qs = item.get("questions") or []
            if isinstance(qs, list):
                for q in qs[:3]:
                    q_text = str(q or "").strip()
                    if q_text:
                        qa.append(f"Q: {q_text}")
            for token in item.get("style_targets") or []:
                t = str(token or "").strip()
                if t and t not in style_targets:
                    style_targets.append(t)
            for token in item.get("memory_targets") or []:
                t = str(token or "").strip()
                if t and t not in memory_targets:
                    memory_targets.append(t)
        elif role == "user":
            a = str(item.get("content") or "").strip()
            if a:
                qa.append(f"A: {a}")

    preferred_language = str(state.get("preferred_language") or "en").lower()
    source_language = str(state.get("source_language") or preferred_language or "en").lower()
    translation_mode = str(state.get("translation_mode") or "follow_input")
    is_en = preferred_language == "en"

    question_prefix = "Q" if is_en else "问"
    answer_prefix = "A" if is_en else "答"
    qa_localized: List[str] = []
    for line in qa:
        if line.startswith("Q: "):
            qa_localized.append(f"{question_prefix}: {line[3:]}")
        elif line.startswith("A: "):
            qa_localized.append(f"{answer_prefix}: {line[3:]}")
        else:
            qa_localized.append(line)

    header = "[WriteClaw generation brief]" if is_en else "[WriteClaw 生成简报]"
    language_profile = (
        "[language profile]\n"
        f"preferred_output_language: {preferred_language}\n"
        f"source_language: {source_language}\n"
        f"translation_mode: {translation_mode}"
        if is_en
        else "[语言配置]\n"
        f"首选输出语言: {preferred_language}\n"
        f"源语言: {source_language}\n"
        f"翻译模式: {translation_mode}"
    )
    style_block = ""
    if style_targets:
        style_block = (
            "\n\n[style targets]\n" if is_en else "\n\n[风格目标]\n"
        ) + "\n".join(f"- {item}" for item in style_targets[:10])
    memory_block = ""
    if memory_targets:
        memory_block = (
            "\n\n[memory targets]\n" if is_en else "\n\n[记忆目标]\n"
        ) + "\n".join(f"- {item}" for item in memory_targets[:10])
    execution_header = "[execution preference]" if is_en else "[执行偏好]"
    execution_block = (
        f"\n\n{execution_header}\n"
        f"generation_scope: {generation_preferences['generation_scope']}\n"
        f"requested_chapters: {generation_preferences['requested_chapters'] or 'auto'}\n"
        f"chapter_pause_mode: {generation_preferences['chapter_pause_mode']}\n"
        f"user_request: {generation_preferences['user_request'] or '-'}"
    )
    if qa_localized:
        qa_text = "\n".join(qa_localized[-16:])
        qa_header = "[recent ideation QA]" if is_en else "[最近构思问答]"
        return f"{header}\n{refined}\n\n{language_profile}{style_block}{memory_block}{execution_block}\n\n{qa_header}\n{qa_text}".strip()
    return f"{header}\n{refined}\n\n{language_profile}{style_block}{memory_block}{execution_block}".strip()
