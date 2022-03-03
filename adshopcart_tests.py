import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdvantageShoppingCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def new_test():
        methods.setUp()
        methods.check_homepage()
        methods.check_contact_us()
        methods.register()
        methods.log_out()
        methods.log_in()
        methods.delete_user()
        methods.tearDown()
###################################################_END_OF_TESTS_#######################################################



