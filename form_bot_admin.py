import os

import abstra.forms as af

from env import ADMIN_EMAIL
from telegram import TelegramBot

bot = TelegramBot()
user = af.get_user()

if user.email != ADMIN_EMAIL:
    bot.send_message(f"{user.email} tentou acessar o bot")
    raise Exception("User not allowed")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
TG_WEBHOOK_TOKEN = os.environ.get("TG_WEBHOOK_TOKEN")

if not TG_BOT_TOKEN or not TG_WEBHOOK_TOKEN:
    raise ValueError("TG_BOT_TOKEN or TG_WEBHOOK_TOKEN are not set")

page_res = (
    af.Page()
    .read("URL")
    .display_markdown(
        f""""
- TG_BOT_TOKEN: {TG_BOT_TOKEN}
- TG_WEBHOOK_TOKEN: {TG_WEBHOOK_TOKEN}
"""
    )
    .run()
)

bot.setup_webhook(f"{page_res['URL']}")

bot.send_message("bot reconfigurado com sucesso!")
