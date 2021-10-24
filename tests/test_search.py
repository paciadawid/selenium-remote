import unittest
import HtmlTestRunner

from pages.basket import BasketPage
from pages.home import HomePage
from pages.search import SearchPage
from utils.driver_creator import create_driver

from hamcrest import *

from time import sleep

class SearchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver()

        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.basket_page = BasketPage(self.driver)

    def test_search_no_item(self):
        self.home_page.search_item("test")
        self.search_page.check_if_alert_appear()

    def test_check_dresses(self):
        self.home_page.search_item("dress")
        assert_that(self.search_page.get_all_elements(), has_length(7))

    def test_add_1st_dress_to_cart(self):
        self.home_page.search_item("dress")
        self.search_page.add_element_to_basket()
        self.search_page.proceed_to_checkout()
        assert_that(self.basket_page.get_total_price(), greater_than(20))
        assert_that(self.basket_page.get_shipping_price(), equal_to(2))

    def test_add_2_different_items(self):
        self.home_page.search_item("dress")
        self.search_page.add_element_to_basket()
        self.search_page.continue_shopping()

        self.home_page.search_item("Blouse")
        self.search_page.add_element_to_basket()
        self.search_page.proceed_to_checkout()

        assert_that(self.basket_page.get_total_price(), greater_than(50))
        assert_that(self.basket_page.get_shipping_price(), equal_to(2))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
