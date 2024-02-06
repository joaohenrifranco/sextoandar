from typing import List

import abstra.tables as at
import abstra.workflows as aw

from telegram import TelegramBot
from zap import ZapAPI

chat_id = aw.get_data("chat_id")
bot = TelegramBot(chat_id=chat_id)

zap = ZapAPI()


def run_scraping() -> None:
    listing_results = zap.fetch_listings()

    print("Analyzing listings...")

    urls: List[str] = []

    old_listings = at.select("listings_urls")

    bot.send_message(f"tu já viu {len(old_listings)} anúncios")
    bot.send_message(f"catei {len(listing_results)} anúncios no zap")

    for listing_result in listing_results:
        if listing_result.listing.id in [l["zap_id"] for l in old_listings]:
            continue
        
        url = zap.make_listing_url(listing_result.listing)

        print(f"New listing found: {listing_result.listing.id}")
        bot.send_message(f"se liga nesse {url}")

        try:
            at.insert(
                "listings_urls",
                {
                    "zap_id": listing_result.listing.id,
                    "url": url,
                },
            )
        except Exception as e:
            print("Error inserting listing:")
            print(e)
            continue



bot.send_message("dando uma olhada aqui")
urls = run_scraping()
bot.send_message("por agora é isso")


try:
    at.delete("locks", {"chat_id": chat_id})
except Exception:
    raise Exception(f"Delete lock failed for chat_id {chat_id}")
