import os
from typing import Optional

def get_env_variable(name: str) -> str:
    value = os.environ.get(name)
    if value is None:
        raise ValueError(f"{name} is not set")
    return value

TG_WEBHOOK_TOKEN = get_env_variable("TG_WEBHOOK_TOKEN")
TG_BOT_TOKEN = get_env_variable("TG_BOT_TOKEN")
TG_OWNER_CHAT_ID = get_env_variable("TG_OWNER_CHAT_ID")
ADMIN_EMAIL = get_env_variable("ADMIN_EMAIL")
