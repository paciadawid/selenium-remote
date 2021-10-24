from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base import BasePage


class MyCreditSlipsPage(BasePage):

    no_credit_slips_alert_selector = (By.CSS_SELECTOR, ".alert.alert-warning")

    def check_if_no_alert(self):
        try:
            self.check_invisibility_of_element(self.no_credit_slips_alert_selector)
        except TimeoutException:
            self.driver.save_screenshot("check_if_no_alert.png")