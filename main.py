"""
主程序入口
"""
import datetime
import json
import os
import sys
import traceback

from config import Config
from utils.language_detector import detect_language
from workflow.executor import CompositiveExecutor


def _ensure_utf8_stdio() -> None:
    for stream_name in ("stdin", "stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None or not hasattr(stream, "reconfigure"):
            continue
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            continue


def _default_initial_knowledge(language: str) -> str:
    if str(language or "").lower().startswith("en"):
        return """
        Long-form fiction guidance:
        1. Keep the world model explicit and stable.
        2. Give characters clear motives, pressure, and growth.
        3. Land conflict, escalation, and payoff in each chapter.
        4. Protect continuity across facts, tone, and causal logic.
        """
    return """
    科幻小说创作要点：
    1. 世界观设定要完整，包括科技水平、社会结构、时间背景
    2. 人物要有深度，动机要清晰
    3. 情节要有冲突和高潮
    4. 保持逻辑一致性
    """


def main():
    """主函数"""
    _ensure_utf8_stdio()

    try:
        config = Config(require_api_key=False)
        text = (lambda zh, en: en if str(getattr(config, "language", "auto") or "auto").lower().startswith("en") else zh)

        print("=" * 60)
        print(text("协同式 RAG-Agent 长文本生成系统", "Collaborative RAG-Agent Long-Form Writer"))
        print("=" * 60)
        print()

        if not config.api_key:
            print(text("错误：未检测到 API Key。", "Error: API key not found."))
            print(text("请在 .env 或环境变量中配置以下之一：", "Configure one of the following in `.env` or environment variables:"))
            print("  DEEPSEEK_API_KEY / OPENAI_API_KEY / CODEX_API_KEY")
            return

        user_idea = input("请输入你的创意想法（留空使用示例） / Enter your story idea (leave blank for an example): ").strip()
        if not user_idea:
            user_idea = text(
                "一个关于未来世界AI觉醒的科幻故事，风格细腻宏大，探讨人工智能与人类的关系",
                "A science-fiction story about AI awakening in a future world, lyrical and epic in tone, exploring the relationship between artificial intelligence and humanity.",
            )
            print(f"\n{text('使用示例 idea', 'Using sample idea')}: {user_idea}")
        else:
            print(f"\n{text('收到自定义 idea', 'Received custom idea')}: {user_idea}")

        detected_language = detect_language(user_idea)
        config.language = detected_language
        text = (lambda zh, en: en if detected_language == "en" else zh)

        # 仅启用动态 memory（禁用静态 RAG / 静态知识库）
        config.memory_only_mode = True
        config.enable_rag = False
        config.enable_static_kb = False

        if not config.run_id:
            config.run_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        if config.memory_reset_each_run:
            config.memory_vector_db_path = os.path.join(
                config.vector_db_path,
                "memory",
                f"run_{config.run_id}",
            )

        os.makedirs(config.memory_vector_db_path, exist_ok=True)
        run_dir = os.path.join(config.runs_dir, config.run_id)
        os.makedirs(run_dir, exist_ok=True)

        print(f"\n{text('[启动配置]', '[Startup Config]')}")
        print(f"- run_id: {config.run_id}")
        print(f"- provider/model: {config.llm_provider}/{config.model_name}")
        mode_label = "memory-only" if config.memory_only_mode else "full-rag"
        print(f"- {text('模式', 'Mode')}: {text('仅动态记忆', mode_label) if config.memory_only_mode else text('完整 RAG', mode_label)}")
        print(f"- dynamic_memory: {config.memory_vector_db_path}")
        print(f"- runs_dir: {run_dir}")
        print("-" * 60)

        executor = CompositiveExecutor(config)

        # ---- OpenClaw interactive hook ----
        # If claw mode is on, let the agent pause and ask the user questions.
        if config.execution_mode == "claw":
            def _user_interaction_hook(question: str) -> str:
                print(f"\n[OpenClaw] 🤔 Agent question: {question}")
                try:
                    return input("  ↳ Your answer: ").strip() or "(skipped)"
                except (EOFError, KeyboardInterrupt):
                    return "(skipped)"
            # Patch the hook into the executor so claw_manager picks it up
            executor._claw_user_interaction_hook = _user_interaction_hook
        # -----------------------------------

        initial_knowledge = _default_initial_knowledge(config.language)

        print(text("[阶段] 开始生成长文本（终端将持续输出进度）...", "[Stage] Generating long-form text (progress will stream in the terminal)..."))
        print("-" * 60)
        result = executor.generate_long_text(
            idea=user_idea,
            initial_knowledge=initial_knowledge,
            auto_analyze=True,
        )
        result_language = str(result.get("language") or detected_language or config.language or "en").lower()
        text = (lambda zh, en: en if result_language.startswith("en") else zh)

        print("\n" + "=" * 60)
        print(text("生成完成", "Generation complete"))
        print("=" * 60)
        print(f"{text('主题', 'Topic')}: {result['topic']}")
        print(f"{text('文本类型', 'Text type')}: {result['text_type']}")
        print(f"{text('文本长度', 'Length')}: {result['length']} {text('字', 'chars')}")
        print(f"{text('迭代次数', 'Iterations')}: {result['iterations']}")
        print(f"{text('已写章节', 'Chapters written')}: {result.get('chapters_written', 0)}")
        if "consistency" in result:
            print(f"{text('一致性分数', 'Consistency score')}: {result['consistency'].get('overall_confidence', 0):.3f}")
        if result.get("progress_log"):
            lines = result["progress_log"].splitlines()
            total_line = [l for l in lines if l.startswith("total_words=")]
            if total_line:
                try:
                    total_words = int(total_line[-1].split("=", 1)[1].strip())
                    print(text(f"总字数: {total_words}", f"Total words: {total_words}"))
                except Exception:
                    print(total_line[-1])

        print(f"\n{text('生成的文本', 'Generated text')}:")
        print("-" * 60)
        print(result["final_text"])
        print("-" * 60)

        output_file = os.path.join(run_dir, "output.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text(f"主题: {result['topic']}\n", f"Topic: {result['topic']}\n"))
            f.write(text(f"文本类型: {result['text_type']}\n", f"Text type: {result['text_type']}\n"))
            f.write(text(f"文本长度: {result['length']} 字\n", f"Length: {result['length']} chars\n"))
            f.write(text(f"迭代次数: {result['iterations']}\n", f"Iterations: {result['iterations']}\n"))
            f.write("\n" + "=" * 60 + "\n")
            f.write(text("生成的文本：\n", "Generated text:\n"))
            f.write("=" * 60 + "\n\n")
            f.write(result["final_text"])
            f.write(text("\n\n[轮次摘要]\n", "\n\n[Round Results]\n"))
            f.write(json.dumps(result.get("round_results", []), ensure_ascii=False, indent=2))

        progress_file = os.path.join(run_dir, "progress.log")
        print(f"\n{text('结果已保存到', 'Saved to')}: {output_file}")
        print(f"{text('进度日志', 'Progress log')}: {progress_file}")
        print(f"{text('动态记忆索引', 'Dynamic memory index')}: {os.path.join(config.memory_vector_db_path, 'memory_index.json')}")
    except KeyboardInterrupt:
        try:
            lang = str(locals().get("detected_language") or locals().get("result_language") or "en")
            print("\nInterrupted by user (CTRL+C)." if lang.startswith("en") else "\n已手动中断（CTRL+C）。")
        except Exception:
            print("\nInterrupted by user (CTRL+C).")
    except Exception as e:
        try:
            lang = str(locals().get("detected_language") or locals().get("result_language") or "en")
            print(f"\n{'Error' if lang.startswith('en') else '错误'}: {str(e)}")
        except Exception:
            print(f"\nError: {str(e)}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
