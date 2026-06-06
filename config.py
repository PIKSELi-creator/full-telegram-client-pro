import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME', 'full_client')

# Дополнительные настройки
DOWNLOAD_PATH = './downloads'
AUTO_REPLY = True
