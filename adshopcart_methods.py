############################################_START_OF_PROGRAM_#########################################################
import datetime
from advantage_shopping_cart import adshopcart_locators as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)

# Defining set up:
def setUp():

    # Maximize browser window after start:
    driver.maximize_window()

    # Let's wait for the browser response in general:
    driver.implicitly_wait(30)

    # Navigating to the Advantage Shopping Cart app website:
    driver.get(locators.asc_url)

    # Checking/comparing the expected current URL address and the expected correct title:
    if driver.current_url == locators.asc_url and driver.title == '\xa0Advantage Shopping':
        print(f'Test Start at: {datetime.datetime.now()}')
        print(f'We\'re at Advantage Shopping Cart homepage -- {driver.current_url} and {driver.title}')
#       print(f'We\'re seeing title page -- {driver.title}')
        print(f'We\'re seeing title logo -- Advantage Demo.')
#       sleep(10)

    else:
        print(f'Opps! The driver current url is as expected but not quite the driver title!')
        driver.close()
        driver.quit()

# Defining teardown if driver is working and not None:
def tearDown():
    if driver is not None:
        print(f'----------------------------------------------')
        print(f'Test End at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

setUp()
tearDown()

#################################################_END_OF_PROGRAM_######################################################





