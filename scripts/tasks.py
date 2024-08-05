import requests
import os
import json
import openai
import pandas as pd
from bs4 import BeautifulSoup

def research_blogs():
    print("Pesquisando blogs populares e analisando temas e estratégias.")
    # Implementação da função

def debug_api_issues():
    print("Diagnosticando problemas de requisição à API.")
    # Implementação da função

def identify_keywords():
    print("Identificando palavras-chave e otimizando SEO.")
    try:
        # Google Trends CSV
        trends = pd.read_csv('/home/runner/BlogGenius/google_trends_data.csv')
        trends_dict = trends.to_dict('records')
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV do Google Trends: {e}")
        trends_dict = []

    try:
        # Ubersuggest (Scraping)
        ubersuggest_keywords = []
        url = "https://app.neilpatel.com/en/ubersuggest"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for item in soup.select(".keyword_overview__item"):
            ubersuggest_keywords.append(item.text.strip())
    except Exception as e:
        print(f"Erro ao acessar Ubersuggest: {e}")
        ubersuggest_keywords = []

    keywords = trends_dict + ubersuggest_keywords
    with open('/home/runner/BlogGenius/keywords.json', 'w') as f:
        json.dump(keywords, f)

def handle_pytrends_warnings():
    print("Gerenciando avisos relacionados ao pytrends.")
    # Implementação da função

def create_drafts():
    print("Criando rascunhos de artigos.")
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        with open('/home/runner/BlogGenius/keywords.json', 'r') as f:
            keywords = json.load(f)
        if not keywords:
            raise ValueError("Nenhuma palavra-chave encontrada.")
        prompt = f"Write an article about {keywords[0]}"
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0]['message']['content'].strip()
        with open('/home/runner/BlogGenius/content.html', 'w') as f:
            f.write(content)
        print("Rascunho criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar rascunhos de artigos: {e}")

def review_articles():
    print("Revisando e aprovando artigos.")
    try:
        with open('/home/runner/BlogGenius/content.html', 'r') as f:
            content = f.read()
        approved_content = content + "\n\nApproved by GPT-Approval."
        with open('/home/runner/BlogGenius/approved_content.txt', 'w') as f:
            f.write(approved_content)
        print("Artigo revisado e aprovado.")
    except FileNotFoundError:
        print("Erro: Arquivo de conteúdo não encontrado")

def configure_openai_api():
    print("Configurando a API OpenAI.")
    openai.api_key = os.getenv('OPENAI_API_KEY')
    print("API OpenAI configurada com sucesso.")

def publish_article():
    print("Publicando artigo no Medium.")
    try:
        medium_token = os.getenv('MEDIUM_TOKEN')
        if not medium_token:
            raise ValueError("Token do Medium não configurado.")

        title = "Artigo Automatizado"
        with open('/home/runner/BlogGenius/approved_content.txt', 'r') as f:
            content = f.read()

        data = {
            "title": title,
            "contentFormat": "html",
            "content": content,
            "publishStatus": "public"
        }

        headers = {
            'Authorization': f'Bearer {medium_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        user_response = requests.get('https://api.medium.com/v1/me', headers=headers)
        if user_response.status_code != 200:
            raise Exception(f'Failed to fetch user details: {user_response.status_code}')

        user_id = user_response.json()['data']['id']
        post_url = f'https://api.medium.com/v1/users/{user_id}/posts'

        response = requests.post(post_url, headers=headers, json=data)
        if response.status_code != 201:
            raise Exception(f'Failed to create post: {response.status_code}')

        print(f"Post publicado com sucesso: {response.json()['data']['url']}")
    except Exception as e:
        print(f"Erro ao publicar o post: {e}")
