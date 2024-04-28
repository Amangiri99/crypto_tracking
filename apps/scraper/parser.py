from selenium.webdriver.common.by import By

class CoinMarketParser:
    """
    Class to parse the html content
    """
    def __init__(self, htmlElement):
        self.htmlElement = htmlElement

    def __is_positive_trend(self, table_row):
        """
        Checks if the span contains class that refers to positive trend
        """
        child_span_element = table_row.find_element(By.CSS_SELECTOR, 'span > span')

        # Get the class name of the child span element
        class_name = child_span_element.get_attribute('class')
        return "icon-Caret-up" in class_name 

    def get_name(self):
        """
        Parse the crypto names from html elements.
        """
        crypto_name = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)")
        crypto_full_name = crypto_name.find_elements(By.TAG_NAME, "p")
        name = crypto_full_name[0].text
        short_name = crypto_full_name[1].text
        return name, short_name
    
    def get_price(self):
        """
        Parse the crypto price from html elements
        """
        crypto_price = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(4)")
        return crypto_price.text
    
    def get_one_hour_change(self):
        """
        Parse the crypto one hour change from html elements
        """
        crypto_one_hour_change = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(5)")
        if not self.__is_positive_trend(crypto_one_hour_change):
            return f"-{crypto_one_hour_change.text}"
        return crypto_one_hour_change.text

    def get_one_day_change(self):
        """
        Parse the crypto one day change from html elements
        """
        crypto_one_day_change = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(6)")
        if not self.__is_positive_trend(crypto_one_day_change):
            return f"-{crypto_one_day_change.text}"
        return crypto_one_day_change.text
    
    def get_one_week_change(self):
        """
        Parse the crypto one week change from html elements
        """
        crypto_one_week_change = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(7)")
        if not self.__is_positive_trend(crypto_one_week_change):
            return f"-{crypto_one_week_change.text}"
        return crypto_one_week_change.text

    def get_market_cap(self):
        """
        Parse the crypto market cap from html elements
        """
        crypto_market_cap = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(8)")
        return crypto_market_cap.text

    def get_volume(self):
        """
        Parse the crypto volume relative to dollar and the coin cap from html elements
        """
        crypto_volume = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(9)")
        crypto_volume_info = crypto_volume.find_elements(By.TAG_NAME, "p")
        trade_in_dollars = crypto_volume_info[0].text
        trade_in_crypto = crypto_volume_info[1].text
        return trade_in_dollars, trade_in_crypto
    
    def get_circulating_supply(self):
        """
        Parse the circulating supply of the crypto
        """
        crypto_circulating_supply = self.htmlElement.find_element(By.CSS_SELECTOR, "td:nth-of-type(10)")
        return crypto_circulating_supply.text

