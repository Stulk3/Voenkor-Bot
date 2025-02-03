import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv("secrets.env")

# Получаем значение токена
token = os.getenv('BOT_TOKEN')

print(f"Your secret token is: {token}")
