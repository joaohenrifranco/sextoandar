import abstra.hooks as ah
import abstra.workflows as aw
import abstra.tables as at
from env import TG_OWNER_CHAT_ID
from telegram import TelegramBot

body, query, headers = ah.get_request()

chat_id = str(body["message"]["chat"]["id"]) # type: ignore
bot = TelegramBot(chat_id)

aw.set_data("chat_id", chat_id)

try:
    at.insert("locks", {"chat_id": chat_id})
except Exception:
    bot.send_message("calma")
    ah.send_response("success", 200, {"Content-Type": "text/plain"})
    raise Exception(f"Already for chat_id {chat_id}")

bot.send_message("e ai")

print("Body", body)
print("Query", query)
print("Headers", headers)

if chat_id != TG_OWNER_CHAT_ID:
    bot.send_message("não posso falar com você")
    raise Exception("Unauthorized")



ah.send_response("success", 200, {"Content-Type": "text/plain"})