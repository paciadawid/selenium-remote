from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):

    search_field_selector = (By.ID, "search_query_top")
    search_button_selector = (By.NAME, "submit_search")

    def search_item(self, item):
        element = self.driver.find_element(*self.search_field_selector)
        element.clear()
        element.send_keys(item)
        self.driver.find_element(*self.search_button_selector).click()
