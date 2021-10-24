from selenium.webdriver.common.by import By

from pages.base import BasePage


class MyAddressesPage(BasePage):

    addresses_selector = (By.CSS_SELECTOR, ".bloc_adresses div")

    def check_if_any_addresses(self):
        self.driver.find_element(*self.addresses_selector)
