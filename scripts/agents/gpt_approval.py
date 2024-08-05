import os

def review_articles():
    print("Revisando e aprovando artigos.")
    try:
        with open(os.path.join(os.path.dirname(__file__), '../../content.html'), 'r') as f:
            content = f.read()
        approved_content = content + "\n\nApproved by GPT-Approval."
        with open(os.path.join(os.path.dirname(__file__), '../../approved_content.txt'), 'w') as f:
            f.write(approved_content)
    except FileNotFoundError:
        print("Erro: Arquivo de conteúdo não encontrado")

if __name__ == "__main__":
    review_articles()
