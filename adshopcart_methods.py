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

    else:
        print(f'Opps! The driver current url is as expected but not quite the driver title!')
        driver.close()
        driver.quit()


# Checking the homepage section:
def check_homepage():
    if driver.current_url == locators.asc_url:
        print(f'You\'re on the Advantage Shopping Cart homepage.')
        sleep(1)
    else:
        print(f'This is unexpected, Check your code.')
    if driver.current_url == locators.asc_url:
        assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'miceTxt').is_displayed()
        sleep(2)
        print(f'You\'ve just checked SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts.')
        driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
        print(f'Checked: OUR PRODUCTS.')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        print(f'Checked: SPECIAL OFFER.')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        print(f'Checked: POPULAR ITEMS.')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        print(f'Browsed: CONTACT US.')
        sleep(0.25)


# Exploring Contact Us section:
def check_contact_us():
    if driver.current_url == locators.asc_url:
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//*[name='productListboxContactUs']")).select_by_visible_text('HP Chromebook 14 G1(ENERGY STAR)')
        sleep(0.5)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
        driver.find_element(By.ID, 'send_btnundefined').click()
        print(f'Checked CONTACT US section!')


# Creating a new Advantage Shopping Cart account:
def register():
    if driver.current_url == locators.asc_url:
        driver.find_element(By.ID, "menuUser").click()
        sleep(5)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == locators.asc_create_url:
            assert driver.find_element(By.XPATH, '//h3[contains(.,"CREATE ACCOUNT")]').is_displayed()
            print(f'Check: "CREATE NEW ACCOUNT"')
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, "[name='usernameRegisterPage']").send_keys(locators.username)
            driver.find_element(By.CSS_SELECTOR, "[name='emailRegisterPage']").send_keys(locators.email)
            driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']").send_keys(locators.password)
            driver.find_element(By.CSS_SELECTOR, "[name='confirm_passwordRegisterPage']").send_keys(locators.password)
            driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
            driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
            driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
            driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
            driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
            driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
            driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
            sleep(1)
            driver.find_element(By.NAME, 'i_agree').click()
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(0.5)
            if driver.find_element(By.ID, 'menuUser').is_displayed():
                print(f'User is created {locators.full_name} and {locators.email}')
                sleep(3)
            else:
                print(f'User is not created. Check your code')
            driver.find_element(By.ID, "menuUser").click()
            sleep(1)
            driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
            sleep(0.25)
            print(f'{locators.full_name}')
            sleep(5)
            driver.find_element(By.ID, "menuUser").click()
            sleep(1)
            driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
            sleep(0.25)
            print(f'Check: "NO ORDERS".')
            sleep(5)


def log_out():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(3)
    if driver.current_url == locators.asc_url:
        print(f'User {locators.full_name}--{locators.email} Sign out')
        sleep(1)
    else:
        print(f'Error message')

def log_in():
    if driver.current_url == locators.asc_url:
        driver.find_element(By.ID, "menuUser").click()
        sleep(0.25)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        print(f'User {locators.full_name}--{locators.email} logged in ')
        sleep(1)
    else:
        print(f'Error message')


def delete_user():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(5)
    print(f'Check: "DELETE ACCOUNT" for {locators.username}')
    sleep(5)


def login_with_deleted_cred():
    driver.find_element(By.ID, "menuUser").click()
    sleep(0.25)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    if driver.find_element(By.ID, 'signInResultMessage'):
        print(f'Incorrect user name or password.')
    else:
        print(f'Check: Account Validated.')


# Defining teardown if driver is working and not None:
def tearDown():
    if driver is not None:
        print(f'----------------------------------------------')
        print(f'Test End at: {datetime.datetime.now()}')
        driver.close()
        sleep(0.25)
        driver.quit()


# Calls section:
setUp()
register()
log_out()
log_in()
check_homepage()
check_contact_us()
log_out()
delete_user()
login_with_deleted_cred()
tearDown()

###################################################_END_OF_METHODS_###################################################

