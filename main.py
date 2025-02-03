import os
from dotenv import load_dotenv

   # Загружаем переменные из файла .env
load_dotenv()

   # Получаем значение токена
token = os.getenv('BOT_TOKEN')

print(f"Your secret token is: {token}")   
