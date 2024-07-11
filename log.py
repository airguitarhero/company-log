import requests
from dotenv import load_dotenv
import os

load_dotenv()
failed_ideas = 99
api_key = 'ai_rulez_lizzm'
url = f'https://www.tensinet.tech/secret?key={api_key}'
secret = requests.get(url)
