import os

import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("MARKET_TOKEN")
CHAT_ID: int = int(os.getenv("CHAT_ID"))

bot = telebot.TeleBot(TOKEN)


def send_message(message):
    bot.send_message(CHAT_ID, message)
