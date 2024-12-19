import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_IDS = os.getenv('CHAT_IDS').split(',')

def send_telegram_message(message: str):
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN is not set in the environment variables.")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    for chat_id in CHAT_IDS:
        payload = {
            "chat_id": chat_id,
            "text": message
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print(f"Message sent to chat_id {chat_id}")
        except requests.RequestException as e:
            print(f"Error sending message to chat_id {chat_id}: {e}")
            return False
    
    return True

# CHAT_ID = [1664680026, 1199609382]

# def send_telegram_message(message: str):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": message
#     }

#     try:
#         response = requests.post(url, json=payload)
#         response.raise_for_status()
#         return True
#     except Exception as exs:
#         print(f"Error: exs")
#         return False