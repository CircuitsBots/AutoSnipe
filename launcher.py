import os

import dotenv

from app.bot import AutoSnipe

bot = AutoSnipe(".")
dotenv.load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)
