import logging
import requests
import json
from decouple import config

from apps.scraper import scraper as scrappers 

logger = logging.getLogger('Scrapper Tasks')

def scrape_data_from_coin_market():
    """
    Task to scrape data from coin market at intervals
    """
    logger.info("Starting the task to scrape data from coin market")
    scraper = scrappers.CoinMarketScraper()
    crypto_details = scraper.parse_by_pagination()
    payload = json.dumps({"data": crypto_details})
    response = requests.post(
        url=config("APPLICATION_ENDPOINT"),
        data=payload,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        logger.error(
            "['SCRAPE COIN MARKET TASK'] Response other than 200 received",
            extra={"status_code": response.status_code, "details": response.json()}
        )
    logger.info("Task Completed")
