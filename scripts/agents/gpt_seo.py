import json
import pandas as pd
from bs4 import BeautifulSoup

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

    # Salvar keywords.json na raiz do projeto
    with open('/home/runner/BlogGenius/keywords.json', 'w') as f:
        json.dump(keywords, f)

if __name__ == "__main__":
    identify_keywords()
