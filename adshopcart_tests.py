import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdvantageShoppingCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_asc_user():
        methods.setUp()
        methods.register()
        methods.log_out()
        methods.log_in()
        methods.check_homepage()
        methods.check_contact_us()
        methods.delete_user()
        methods.login_with_deleted_cred()
        methods.tearDown()
###################################################_END_OF_TESTS_#######################################################



