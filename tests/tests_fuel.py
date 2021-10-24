import unittest

import HtmlTestRunner

from python_basics.functions import calculate_fuel
from hamcrest import *


class TestFuel(unittest.TestCase):

    def test_simple_positive(self):
        assert_that(calculate_fuel(12), equal_to(2))

    def test_large_value(self):
        assert_that(calculate_fuel(100756), equal_to(33583))

    def test_negative_value(self):
        assert_that(calculate_fuel(-1), equal_to(False))

    def test_string(self):
        assert_that(calculate_fuel("aaa"), equal_to(False))

    def test_string_number(self):
        assert_that(calculate_fuel("12"), equal_to(2))

    def test_1(self):
        assert_that(calculate_fuel(1), equal_to(1))

    def test_8(self):
        assert_that(calculate_fuel(8), equal_to(1))

    def test_9(self):
        assert_that(calculate_fuel(9), equal_to(1))


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
