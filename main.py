import os
from dotenv import load_dotenv
from bot import Bot

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)
bot.run()