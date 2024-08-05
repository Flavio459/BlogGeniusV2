import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

def create_drafts():
    try:
        print("Criando rascunhos de artigos.")
        openai.api_key = os.getenv('OPENAI_API_KEY')
        with open(os.path.join(os.path.dirname(__file__), '../../keywords.json'), 'r') as f:
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
        with open(os.path.join(os.path.dirname(__file__), '../../content.html'), 'w') as f:
            f.write(content)
        print("Rascunho criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar rascunhos de artigos: {e}")

if __name__ == "__main__":
    create_drafts()
