import openai
import os
import json

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

        if 'choices' in response and len(response['choices']) > 0:
            content = response.choices[0]['message']['content'].strip()
            formatted_content = format_content_as_html(content)
            with open('/home/runner/BlogGenius/content.html', 'w') as f:
                f.write(formatted_content)
            print("Rascunho criado com sucesso.")
        else:
            print("Erro: Resposta da API não contém rascunho.")
    except Exception as e:
        print(f"Erro ao criar rascunhos de artigos: {e}")

def format_content_as_html(content):
    """Formata o conteúdo para HTML, adequado para publicação no Medium."""
    lines = content.split('\n')
    formatted_lines = []

    for line in lines:
        if line.startswith('# '):
            formatted_lines.append(f'<h1>{line[2:].strip()}</h1>')
        elif line.startswith('## '):
            formatted_lines.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith('### '):
            formatted_lines.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith('- '):
            formatted_lines.append(f'<li>{line[2:].strip()}</li>')
        else:
            formatted_lines.append(f'<p>{line.strip()}</p>')

    in_list = False
    final_content = []
    for line in formatted_lines:
        if line.startswith('<li>'):
            if not in_list:
                final_content.append('<ul>')
                in_list = True
            final_content.append(line)
        else:
            if in_list:
                final_content.append('</ul>')
                in_list = False
            final_content.append(line)
    if in_list:
        final_content.append('</ul>')

    return ''.join(final_content)

if __name__ == "__main__":
    create_drafts()
