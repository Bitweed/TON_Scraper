import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID: int = int(os.getenv("CHAT_ID"))

bot = telebot.TeleBot(TOKEN)


def send_message(message):
    bot.send_message(CHAT_ID, f"1 TON - {message}$")
