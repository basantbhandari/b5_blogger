import config
import requests

def create_article(title, content, tags):
    url = f'{config.HASH_NODE_API_ENDPOINT}'
    headers = {
        'Authorization': f'Bearer {config.HASH_NODE_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'title': title,
        'content': content,
        'tags': tags,
        'publicationStatus': 'PUBLISHED',
        'isRepublished': False,
    }
    response = requests.post(url , headers=headers, json=data)
    response.raise_for_status()
    return response.json()['data']