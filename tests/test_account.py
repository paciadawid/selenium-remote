import unittest

import HtmlTestRunner
import xmlrunner

from pages.account import AccountPage
from pages.login import LoginPage
from pages.my_addresses import MyAddressesPage
from pages.my_credit_slips import MyCreditSlipsPage
from utils.driver_creator import create_driver


class AccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver()

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.my_addresses_page = MyAddressesPage(self.driver)
        self.my_credit_slips_page = MyCreditSlipsPage(self.driver)

    def test_addresses_and_credit_slips(self):
        self.login_page.login("seleniumremote@gmail.com", "test123")
        self.account_page.go_to_addresses()
        self.my_addresses_page.check_if_any_addresses()
        self.my_addresses_page.back_to_account_page()
        self.account_page.go_to_credit_slips()
        self.my_credit_slips_page.check_if_no_alert()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
