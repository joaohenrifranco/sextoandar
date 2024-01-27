import requests
from env import TG_BOT_TOKEN, TG_WEBHOOK_TOKEN, TG_OWNER_CHAT_ID
from typing import Any



class TelegramBot:
    def __init__(self, chat_id: Any = TG_OWNER_CHAT_ID):
        self.chat_id = chat_id or TG_OWNER_CHAT_ID

    def setup_webhook(self, url: str) -> None:
        res = requests.get(
            f"https://api.telegram.org/bot{TG_BOT_TOKEN}/setWebhook?url={url}&secret_token={TG_WEBHOOK_TOKEN}"
        )

        res.raise_for_status()

    def send_message(self, message: str) -> None:
        res = requests.get(
            f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?text={message}&chat_id={self.chat_id}"
        )

        res.raise_for_status()