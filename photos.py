import requests
import os
from dotenv import load_dotenv
import json
import random

load_dotenv()

access_key = os.getenv(str('API_KEY'))

def get_photo(query):
    url = f'https://api.unsplash.com/search/photos?query={query}'
    headers = {'Authorization': f'Client-ID {access_key}'}
    response = requests.get(url, headers=headers)
    photo_data = json.loads(response.text)['results']
    random_photo = random.choice(photo_data)
    photo_url = random_photo['urls']['regular']
    return photo_url


