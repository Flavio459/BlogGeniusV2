import requests
import os

def post_to_medium(token, title, content, tags=[]):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    user_response = requests.get('https://api.medium.com/v1/me', headers=headers)

    if user_response.status_code != 200:
        raise Exception(f'Failed to fetch user details: {user_response.status_code}')

    user_id = user_response.json()['data']['id']
    post_url = f'https://api.medium.com/v1/users/{user_id}/posts'

    post_data = {
        'title': title,
        'contentFormat': 'html',
        'content': content,
        'tags': tags,
        'publishStatus': 'public'
    }

    response = requests.post(post_url, headers=headers, json=post_data)

    if response.status_code != 201:
        raise Exception(f'Failed to create post: {response.status_code}')

    return response.json()

def publish_article():
    try:
        medium_token = os.getenv('MEDIUM_TOKEN')
        if not medium_token:
            raise ValueError("Token do Medium não configurado.")

        title = "Artigo Automatizado"
        with open('/home/runner/BlogGenius/content.html', 'r') as f:
            content = f.read()

        tags = ['Automação', 'Inteligência Artificial', 'Redes Neurais', 'Tecnologia', 'Inovação']
        post_response = post_to_medium(medium_token, title, content, tags)
        print(f"Post publicado com sucesso: {post_response['data']['url']}")
    except Exception as e:
        print(f"Erro ao publicar o post: {e}")

if __name__ == "__main__":
    publish_article()
