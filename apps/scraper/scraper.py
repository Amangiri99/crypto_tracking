import logging
import time
from pathlib import Path
from decouple import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from apps.scraper import parser as scraper_parsers

logger = logging.getLogger('Scrapper')


class BaseWebScraper:
    """
    Base Class for a scraper to request data from external sources
    """
    def __init__(self, url):
        self.webdriver_path = Path(__file__).resolve().parent.parent.parent / 'chromedriver'
        self.driver = webdriver.Chrome()
        self.url = url

    def get_web_driver_instance(self, query_params=""):
        """
        Function to open the requested site using the driver
        """
        return self.driver.get(f"{self.url}/?{query_params}")
    
    def quit_driver_instance(self):
        """
        Function to quit the web driver api.
        """
        return self.driver.quit()


class CoinMarketScraper(BaseWebScraper):
    """
    Class to fetch data from coin market and parse the returned response.
    """
    def __init__(self):
        self.current_height = 0
        self.total_rows_per_page = config("TOTAL_TABLE_ROWS_PER_PAGE", cast=int)
        self.batch_size_to_process = config("SCRAPING_BATCH_SIZE", cast=int)
        super().__init__(url=config("COIN_MARKET_URL"))
    
    def scroll_down(self, new_height):
        """
        Function to scroll down the page using JavaScript.
        """
        self.driver.execute_script(
            "window.scrollTo({current_height}, {new_height});".format(current_height=self.current_height,new_height=new_height)
        )
        self.current_height = new_height
    
    def get_page_height(self):
        """
        Get the height of the entire webpage.
        """
        return self.driver.execute_script("return document.body.scrollHeight")

    def __scrape_coin_market(self):
        """
        Function to parse the response received from the external source.
        """
        # Using the total page length calculate the scroll speed.
        total_iterations = self.total_rows_per_page / self.batch_size_to_process-1
        scroll_increment = self.get_page_height() // total_iterations
        # Keep track of the number of iterations
        num_of_iterations = 0
        parsed_results = []
        while num_of_iterations < total_iterations:
            new_height = num_of_iterations * scroll_increment
            # Scroll the page down
            self.scroll_down(new_height)
            # Explicit wait until the next batch of rows is loaded
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.cmc-table tbody tr:nth-of-type({})'
                     .format(self.batch_size_to_process * (num_of_iterations + 1))))
            )

            # Selecting the table based on the css class.
            crypto_details_table = self.driver.find_element(By.CSS_SELECTOR, '.cmc-table')
            # Selecting the table body that contains all the details about the crypto coins.
            crypto_details_table_body = crypto_details_table.find_element(By.TAG_NAME, 'tbody')
            crypto_details = crypto_details_table_body.find_elements(By.TAG_NAME, 'tr')
            # Iterating in batches, to parse the crypto coins
            crypto_parsed_html = crypto_details[
                num_of_iterations*self.batch_size_to_process:self.batch_size_to_process*(num_of_iterations+1)
            ]
            for crypto in crypto_parsed_html:
                # Creating a parser object to parse the html.
                crypto_parser = scraper_parsers.CoinMarketParser(crypto)
                name, short_name = crypto_parser.get_name()
                trade_in_dollars, trade_in_crypto = crypto_parser.get_volume()
                crypto_info = {
                    'full_name': name,
                    'short_name': short_name,
                    'price': crypto_parser.get_price(),
                    'one_hour_change': crypto_parser.get_one_hour_change(),
                    'one_day_change': crypto_parser.get_one_day_change(),
                    'one_week_change': crypto_parser.get_one_week_change(),
                    'market_cap': crypto_parser.get_market_cap(),
                    'volume_in_dollars': trade_in_dollars,
                    'volume_in_crypto': trade_in_crypto,
                    'circulating_supply': crypto_parser.get_circulating_supply()
                }
                parsed_results.append(crypto_info)
            num_of_iterations = num_of_iterations + 1
        return parsed_results

    def parse_by_pagination(self):
        """
        Function to parse results from multiple pages.
        """
        current_page = 1
        # Create an instance of the web driver
        self.get_web_driver_instance()
        # List to store all details about the crypto.
        list_of_all_cryptos = []
        
        # Continue till we reach the last page
        while True:
            # Scrape the current page
            list_of_all_cryptos.append(self.__scrape_coin_market())
            current_page = current_page + 1
            # Head on to the next page.
            self.get_web_driver_instance(query_params=f"page={current_page}")
            # Currently only parsing the first two pages.
            if (current_page > 2):
                break
        self.quit_driver_instance()
        return list_of_all_cryptos        
