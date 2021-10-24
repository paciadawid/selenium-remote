from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):

    sign_in_button_selector = (By.CLASS_NAME, "login")
    email_field_selector = (By.ID, "email")
    password_field_selector = (By.ID, "passwd")
    submit_login_button_selector = (By.ID, "SubmitLogin")

    def login(self, email, password):
        self.driver.find_element(*self.sign_in_button_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.submit_login_button_selector).click()
