
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from rag import Rag

class Bot:
    def __init__(self, token:str):
        self.token = token
        self.app = ApplicationBuilder().token(self.token).build()
        self.rag = Rag()

    async def hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = " ".join(context.args)
        await update.message.reply_text(response)

    async def code(self, update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
        await update.message.reply_text("https://github.com/william-man/telegram-bot")

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
        await update.message.reply_text("""
            Commands:
                /hello
                    response: Hello <user_first_name>
                /echo
                    response: <input_text>
                /code
                    response: https://github.com/william-man/telegram-bot
                /query <query>
                    response: <result from llama>
        """)

    async def query(self, update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
        response = self.rag.query(" ".join(context.args))
        await update.message.reply_text(str(response))

    def run(self):
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("hello", self.hello))
        self.app.add_handler(CommandHandler("echo", self.echo))
        self.app.add_handler(CommandHandler("code", self.code))
        self.app.add_handler(CommandHandler("query", self.query))
        print("Running Bot...")
        self.app.run_polling()
