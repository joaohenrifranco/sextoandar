import os

_TG_WEBHOOK_TOKEN = os.environ.get("TG_WEBHOOK_TOKEN")
_TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
_TG_OWNER_CHAT_ID = os.environ.get("TG_OWNER_CHAT_ID")
_ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")

if not _TG_BOT_TOKEN:
		raise ValueError("TG_BOT_TOKEN is not set")

if not _TG_WEBHOOK_TOKEN:
		raise ValueError("TG_WEBHOOK_TOKEN is not set")

if not _TG_OWNER_CHAT_ID:
		raise ValueError("TG_OWNER_CHAT_ID is not set")

if not _ADMIN_EMAIL:
		raise ValueError("ADMIN_EMAIL is not set")

TG_WEBHOOK_TOKEN: str = _TG_WEBHOOK_TOKEN
TG_BOT_TOKEN: str = _TG_BOT_TOKEN
TG_OWNER_CHAT_ID: str = _TG_OWNER_CHAT_ID
ADMIN_EMAIL: str = _ADMIN_EMAIL