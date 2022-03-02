import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdvantageShoppingCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def signUp():
        methods.setUp()
        methods.signUp()
        methods.checkOut()
        methods.tearDown


