from selenium.webdriver.common.by import By

from pages.base import BasePage

from time import sleep


class SearchPage(BasePage):

    alert_box_selector = (By.CSS_SELECTOR, ".alert.alert-warning")
    product_container_selector = (By.CSS_SELECTOR, ".product-container")
    add_to_cart_button_selector = (By.XPATH, "//a[@title='Add to cart']")
    proceed_to_checkout_button_selector = (By.XPATH, "//a[@title='Proceed to checkout']")
    continue_shopping_button_selector = (By.XPATH, "//span[@title='Continue shopping']")


    def check_if_alert_appear(self):
        self.driver.find_element(*self.alert_box_selector)

    def get_all_elements(self):
        elements = self.driver.find_elements(*self.product_container_selector)
        return elements

    def add_element_to_basket(self):
        element = self.driver.find_element(*self.product_container_selector)
        self.hover_mouse_over(element)
        self.driver.find_element(*self.add_to_cart_button_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button_selector).click()

    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button_selector).click()