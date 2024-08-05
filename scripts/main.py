import os
from agents.gpt_content import create_drafts
from agents.medium_posting import publish_article
from agents.gpt_research import research_blogs
from agents.gpt_api_debugger import debug_api_issues
from agents.gpt_seo import identify_keywords
from agents.gpt_pytrends_expert import handle_pytrends_warnings
from agents.gpt_approval import review_articles
from agents.gpt_openai_configurator import configure_openai_api

def run_task(agent_name, task_name):
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
    task_function = tasks.get(task_name)
    if task_function:
        task_function(agent_name=agent_name, task_name=task_name)
    else:
        print(f"Tarefa {task_name} não encontrada.")

def main():
    tasks_to_run = [
        ("GPT-Content", "create_drafts"),
        ("GPT-Approval", "review_articles"),
        ("GPT-Content", "publish_article")
    ]

    for agent_name, task_name in tasks_to_run:
        run_task(agent_name, task_name)

if __name__ == "__main__":
    main()


def run_task(agent_name, task_name):
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
    task_function = tasks.get(task_name)
    if task_function:
        task_function(agent_name=agent_name, task_name=task_name)
    else:
        print(f"Tarefa {task_name} não encontrada.")

def main():
    tasks_to_run = [
        ("GPT-Content", "create_drafts"),
        ("GPT-Approval", "review_articles"),
        ("GPT-Content", "publish_article")
    ]

    for agent_name, task_name in tasks_to_run:
        run_task(agent_name, task_name)

if __name__ == "__main__":
    main()
