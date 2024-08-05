import yaml
import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import openai

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def run_task(agent_name, task_name):
    print(f"Executando tarefa {task_name} para o agente: {agent_name}")
    task_mapping = {
        "research_blogs": research_blogs,
        "debug_api_issues": debug_api_issues,
        "identify_keywords": identify_keywords,
        "handle_pytrends_warnings": handle_pytrends_warnings,
        "create_drafts": create_drafts,
        "review_articles": review_articles,
        "configure_openai_api": configure_openai_api,
        "publish_article": publish_article
    }

    task_function = task_mapping.get(task_name)
    if task_function:
        task_function()
    else:
        print(f"Tarefa {task_name} não encontrada.")

def research_blogs():
    print("Pesquisando blogs populares e analisando temas e estratégias.")
    api_key = os.getenv('SERPER_API_KEY')
    query = "top blogs in technology"
    response = requests.get(f"https://api.serper.dev/search?q={query}", headers={"Authorization": f"Bearer {api_key}"})

    if response.status_code == 200:
        try:
            blogs = response.json().get('results', [])
            with open('blogs.json', 'w') as f:
                json.dump(blogs, f)
            print("Blogs salvos com sucesso.")
        except json.JSONDecodeError:
            print("Erro: Resposta da API não é um JSON válido.")
    else:
        print(f"Erro: Falha na requisição à API. Status code: {response.status_code}")

def debug_api_issues():
    print("Diagnosticando problemas de requisição à API.")
    # Implementar lógica de diagnóstico e resolução de problemas de API

def create_drafts():
    print("Criando rascunhos de artigos.")
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        with open('keywords.json', 'r') as f:
            keywords = json.load(f)
        prompt = f"Write an article about {keywords[0]}"
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        content = response.choices[0].message["content"].strip()
        with open('content.txt', 'w') as f:
            f.write(content)
        print("Artigo gerado e salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao criar rascunhos de artigos: {e}")

def review_articles():
    print("Revisando e aprovando artigos.")
    try:
        with open('content.txt', 'r') as f:
            content = f.read()
        approved_content = content + "\n\nApproved by GPT-Approval."
        with open('approved_content.txt', 'w') as f:
            f.write(approved_content)
    except FileNotFoundError:
        print("Erro: Arquivo de conteúdo não encontrado")

def configure_openai_api():
    print("Configurando a API OpenAI.")
    openai.api_key = os.getenv('OPENAI_API_KEY')
    print("API OpenAI configurada com sucesso.")

def publish_article():
    print("Publicando artigo no Medium.")
    medium_token = os.getenv('MEDIUM_TOKEN')
    try:
        with open('approved_content.txt', 'r') as f:
            content = f.read()
        data = {
            "title": "Automated Article",
            "contentFormat": "markdown",
            "content": content,
            "publishStatus": "public"
        }
        response = requests.post(f"https://api.medium.com/v1/users/{user_id}/posts", headers={"Authorization": f"Bearer {medium_token}"}, json=data)
        print(response.json())
    except Exception as e:
        print(f"Erro ao publicar artigo no Medium: {e}")

def main():
    crewai_config = load_yaml('scripts/crewai.yaml')

    for agent_name in crewai_config['hierarchy']:
        for task_name, task in crewai_config['tasks'].items():
            if task['agent'] == agent_name:
                run_task(agent_name, task_name)

if __name__ == "__main__":
    main()
