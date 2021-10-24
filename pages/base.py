from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def back_to_account_page(self):
        self.driver.back()

    def check_invisibility_of_element(self, selector):
        WebDriverWait(self.driver, 10).until(
             expected_conditions.invisibility_of_element_located(selector))

    def hover_mouse_over(self, selector):
        actions = ActionChains(self.driver)
        actions.move_to_element(selector)
        actions.perform()
