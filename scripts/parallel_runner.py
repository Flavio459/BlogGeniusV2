# scripts/parallel_runner.py
import os
import concurrent.futures
from scripts.agents.gpt_content import create_drafts
from scripts.agents.medium_posting import publish_article
from scripts.agents.gpt_research import research_blogs
from scripts.agents.gpt_api_debugger import debug_api_issues
from scripts.agents.gpt_seo import identify_keywords
from scripts.agents.gpt_pytrends_expert import handle_pytrends_warnings
from scripts.agents.gpt_approval import review_articles
from scripts.agents.gpt_openai_configurator import configure_openai_api

def run_task(task_function, task_name):
    print(f"Executando tarefa {task_name}")
    task_function()

def main():
    tasks = {
        "research_blogs": research_blogs,
        "debug_api_issues": debug_api_issues,
        "identify_keywords": identify_keywords,
        "handle_pytrends_warnings": handle_pytrends_warnings,
        "create_drafts": create_drafts,
        "review_articles": review_articles,
        "configure_openai_api": configure_openai_api,
        "publish_article": publish_article
    }

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for task_name, task_function in tasks.items():
            futures.append(executor.submit(run_task, task_function, task_name))

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Erro na execução de uma tarefa: {e}")

if __name__ == "__main__":
    main()
