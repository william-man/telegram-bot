import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

class Bot:
    def __init__(self, token:str):
        self.token = token
        self.app = ApplicationBuilder().token(self.token).build()

    async def hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = " ".join(context.args)
        await update.message.reply_text(response)

    async def code(self, update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
        await update.message.reply_text("https://github.com/william-man/telegram-bot")

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
        await update.message.reply_text("Hello")

    def run(self):
        self.app.add_handler(CommandHandler("hello", self.hello))
        self.app.add_handler(CommandHandler("echo", self.echo))
        self.app.add_handler(CommandHandler("code", self.code))
        print("Running Bot...")
        self.app.run_polling()

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    bot = Bot(TOKEN)
    bot.run()