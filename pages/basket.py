from selenium.webdriver.common.by import By

from pages.base import BasePage


class BasketPage(BasePage):

    total_price_selector = (By.ID, "total_price")
    total_shipping_selector = (By.ID, "total_shipping")

    def get_total_price(self):
        price_text = self.driver.find_element(*self.total_price_selector).text
        price = float(price_text[1:])
        return price

    def get_shipping_price(self):
        price_text = self.driver.find_element(*self.total_shipping_selector).text
        price = float(price_text[1:])
        return price
