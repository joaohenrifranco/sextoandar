from time import sleep
from typing import List

import abstra.tables as at
import abstra.workflows as aw

from telegram import TelegramBot
from zap import ZapAPI

chat_id = aw.get_data("chat_id")
bot = TelegramBot(chat_id=chat_id)

zap = ZapAPI()


def run_scraping() -> List[str]:
    listing_results = zap.fetch_listings()

    print("Analyzing listings...")

    urls: List[str] = []

    old_listings = at.select("listings_urls")

    for listing_result in listing_results:
        if listing_result.listing.id in [l["zap_id"] for l in old_listings]:
            continue

        print(f"Found listing {listing_result.listing.id}")

        try:
            at.insert(
                "listings_urls",
                {
                    "zap_id": listing_result.listing.id,
                    "url": f"http://www.zapimoveis.com.br/imovel/aluguel/{listing_result.listing.id}/",
                },
            )
        except Exception as e:
            print("Error inserting listing:")
            print(e)
            continue

        urls.append(
            f"http://www.zapimoveis.com.br/imovel/aluguel/{listing_result.listing.id}/"
        )

    return urls


bot.send_message("dando uma olhada aqui")
urls = run_scraping()
bot.send_message("pronto")

if len(urls) == 0:
    bot.send_message("não encontrei nada novo")
else:
    bot.send_message(f"encontrei {len(urls)} novos")

    for index, url in enumerate(urls):
        bot.send_message(url)

        # rate limit
        if index % 10 == 0:
            sleep(10)


try:
    at.delete("locks", {"chat_id": chat_id})
except Exception:
    raise Exception(f"Already for chat_id {chat_id}")
