import requests
from dotenv import load_dotenv
import os

load_dotenv()
failed_ideas = 124
api_key = os.getenv('API_KEY')
url = f'https://www.tensinet.tech/secret?key={api_key}'
secret = requests.get(url)
