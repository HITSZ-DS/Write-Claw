"""
LLM 客户端封装，支持 Codex/OpenAI/DeepSeek（默认指向 packycode Codex）
"""
from typing import List, Dict, Optional, Any
import json
import re
import time
from openai import OpenAI
from config import Config


class LLMClient:
    """LLM API 客户端封装"""
    
    def __init__(self, config: Config):
        self.config = config
        timeout_seconds = getattr(config, "llm_timeout_seconds", 0)
        client_timeout = None if timeout_seconds <= 0 else timeout_seconds
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.api_base_url,
            timeout=client_timeout,
            max_retries=getattr(config, "llm_max_retries", 1),
        )

    def _is_en(self) -> bool:
        return str(getattr(self.config, "language", "auto") or "auto").lower().startswith("en")

    def _text(self, zh: str, en: str) -> str:
        return en if self._is_en() else zh
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        model: Optional[str] = None
    ) -> str:
        """
        调用 LLM 进行对话
        """
        max_t = max_tokens if max_tokens is not None else self.config.max_tokens
        if max_t is None:
            max_t = 2000
        max_t = min(max_t, 8000)
        messages = list(messages)
        if self.config.language.startswith("en"):
            messages.insert(
                0,
                {
                    "role": "system",
                    "content": "You are an English-language assistant. Always respond in English, even if the user prompt mixes other languages.",
                },
            )
        elif self.config.language.startswith("zh"):
            messages.insert(
                0,
                {
                    "role": "system",
                    "content": "你是一名中文助手，请始终使用中文回答，即便用户提示混杂其他语言。",
                },
            )
        try:
            if getattr(self.config, "llm_call_log", True):
                timeout_display = "disabled" if getattr(self.config, "llm_timeout_seconds", 0) <= 0 else f"{getattr(self.config, 'llm_timeout_seconds', 0)}s"
                print(
                    f"[LLM] {self._text('开始', 'start')} provider={self.config.llm_provider} "
                    f"model={model or self.config.model_name} "
                    f"wire={getattr(self.config, 'wire_api', 'chat')} "
                    f"timeout={timeout_display}"
                )
            started = time.perf_counter()
            if getattr(self.config, "wire_api", "chat") == "responses":
                # 将 messages 展开为文本输入，尽量保留角色信息
                joined = "\n".join([f"{m.get('role','user').upper()}: {m.get('content','')}" for m in messages])
                response = self.client.responses.create(
                    model=model or self.config.model_name,
                    input=joined,
                    max_output_tokens=max_t,
                    temperature=temperature if temperature is not None else self.config.temperature,
                    reasoning={"effort": getattr(self.config, "model_reasoning_effort", "high") if hasattr(self.config, "model_reasoning_effort") else "high"},
                )
                output = response.output_text
            else:
                response = self.client.chat.completions.create(
                    model=model or self.config.model_name,
                    messages=messages,
                    temperature=temperature if temperature is not None else self.config.temperature,
                    max_tokens=max_t
                )
                output = response.choices[0].message.content
            if getattr(self.config, "llm_call_log", True):
                cost = time.perf_counter() - started
                print(f"[LLM] {self._text('完成', 'done')} model={model or self.config.model_name} elapsed={cost:.2f}s")
            return output
        except Exception as e:
            if getattr(self.config, "llm_call_log", True):
                cost = time.perf_counter() - started
                print(f"[LLM] {self._text('失败', 'failed')} model={model or self.config.model_name} elapsed={cost:.2f}s err={e}")
            raise Exception(self._text(f"LLM 调用失败: {str(e)}", f"LLM call failed: {str(e)}"))
    
    def chat_with_tools(
        self,
        messages: List[Dict],
        tools: List[Dict],
        temperature: float = 0.2,
        max_tokens: int = 1200,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        真正的 OpenClaw/ReAct 工具调用接口。
        返回 {"content": str, "tool_calls": [{"id", "name", "args"}]}。
        若模型不支持 native tool calling，自动降级为 JSON 文本解析。
        """
        target_model = model or self.config.model_name
        started = time.perf_counter()
        if getattr(self.config, "llm_call_log", True):
            print(f"[Claw] tool-call provider={self.config.llm_provider} model={target_model} tools={[t['function']['name'] for t in tools]}")
        try:
            response = self.client.chat.completions.create(
                model=target_model,
                messages=messages,
                tools=tools,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            msg = response.choices[0].message
            tool_calls = []
            if msg.tool_calls:
                for tc in msg.tool_calls:
                    try:
                        args = json.loads(tc.function.arguments or "{}")
                    except Exception:
                        args = {}
                    tool_calls.append({"id": tc.id, "name": tc.function.name, "args": args})
            if getattr(self.config, "llm_call_log", True):
                elapsed = time.perf_counter() - started
                action = tool_calls[0]["name"] if tool_calls else "text-reply"
                print(f"[Claw] done action={action} elapsed={elapsed:.2f}s")
            return {"content": msg.content or "", "tool_calls": tool_calls}
        except Exception as native_err:
            # 降级：文本模式下要求 LLM 输出 JSON 工具调用
            if getattr(self.config, "llm_call_log", True):
                print(f"[Claw] native tool-call failed ({native_err}), falling back to JSON mode")
            tool_names = [t["function"]["name"] for t in tools]
            tool_descs = "\n".join(
                f'- {t["function"]["name"]}: {t["function"]["description"]}'
                for t in tools
            )
            fallback_messages = list(messages) + [{
                "role": "user",
                "content": (
                    f"Available tools:\n{tool_descs}\n\n"
                    f"Reply ONLY with a JSON object: {{\"tool\": \"<one of {tool_names}>\", \"args\": {{...}}}}"
                ),
            }]
            try:
                raw = self.chat(fallback_messages, temperature=temperature, max_tokens=600, model=target_model)
                m = re.search(r"\{.*\}", raw, re.S)
                if m:
                    parsed = json.loads(m.group(0))
                    tool_name = str(parsed.get("tool") or "").strip()
                    if tool_name in tool_names:
                        elapsed = time.perf_counter() - started
                        if getattr(self.config, "llm_call_log", True):
                            print(f"[Claw] fallback action={tool_name} elapsed={elapsed:.2f}s")
                        return {
                            "content": "",
                            "tool_calls": [{"id": "fb-0", "name": tool_name, "args": parsed.get("args", {})}],
                        }
            except Exception:
                pass
            return {"content": "", "tool_calls": []}

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        生成文本
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        return self.chat(messages, temperature, max_tokens)
