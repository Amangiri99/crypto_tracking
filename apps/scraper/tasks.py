import logging

from apps.scraper import scraper as scrappers 

logger = logging.getLogger('Scrapper Tasks')

def scrape_data_from_coin_market():
    """
    Task to scrape data from coin market at intervals
    """
    logger.info("Starting the task to scrap data from coin market")
    scraper = scrappers.CoinMarketScraper()
    crypto_details = scraper.parse_by_pagination()
    logger.info("Task Completed")
