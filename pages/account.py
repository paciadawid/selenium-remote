from selenium.webdriver.common.by import By

from pages.base import BasePage


class AccountPage(BasePage):

    addresses_button_selector = (By.XPATH, "//a[@title='Addresses']")
    credit_slips_button_selector = (By.XPATH, "//a[@title='Credit slips']")

    def go_to_addresses(self):
        self.driver.find_element(*self.addresses_button_selector).click()

    def go_to_credit_slips(self):
        self.driver.find_element(*self.credit_slips_button_selector).click()

