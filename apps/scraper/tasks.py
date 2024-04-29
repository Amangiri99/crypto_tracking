import logging
import requests
import json
from decouple import config

from apps.celery import app
from apps.scraper import scraper as scrapers

logger = logging.getLogger("Scraper Tasks")

@app.task
def scrape_data_from_coin_market():
    """
    Task to scrape data from coin market at intervals
    """
    logger.info("Starting the task to scrape data from coin market")
    scraper = scrapers.CoinMarketScraper()
    crypto_details = scraper.get_crypto_details_from_multiple_pages()
    payload = json.dumps({"data": crypto_details})
    response = requests.post(
        url=config("APPLICATION_ENDPOINT"),
        data=payload,
        headers={"Content-Type": "application/json"},
        timeout=30
    )
    if response.status_code != 201:
        logger.error(
            "['SCRAPE COIN MARKET TASK API CALL'] Response other than 200 received",
            extra={"status_code": response.status_code, "details": response.json()},
        )
    logger.info("Task Completed")
