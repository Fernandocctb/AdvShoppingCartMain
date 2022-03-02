import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
        print(f'We\'re at Advantage Shopping Cart homepage -- {driver.current_url} with title "{driver.title}" as expected.')
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
        sleep(0.25)
        driver.quit()


def signUP():
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.25)
        assert driver.find_element(By.ID, 'menuUser').is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(.1)
        if driver.current_url == 'https://advantageonlineshopping.com/#/register':
            sleep(0.25)
            driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.asc_username)
            sleep(0.25)
            driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.asc_email)
            sleep(0.25)
            driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.asc_password)
            sleep(0.25)
            driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.asc_password)
            sleep(0.25)
            driver.find_element(By.NAME, 'i_agree').click()
            sleep(0.50)
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(2)

def checkOut():
            driver.find_element(By.XPATH, '//*[@id="menuUser"]').click()
            sleep(5)
#            driver.find_element(By.ID, "hrefUserIcon").click()
#            sleep(.25)
            assert driver.find_element(By.XPATH, '//*[@id="menuUser"]').is_displayed()
            sleep(7)
#            driver.find_element(By.CLASS_NAME, 'My_account').click()
            driver.find_element(By.XPATH, '//span[contains(.,"hi-user")]').click()
            sleep(5)
#            driver.find_element(By.)


setUp()
signUP()
checkOut()
tearDown()