import datetime
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from helpers import functional_helpers


class LostHatTests2(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver\chromedriver.exe")

    @classmethod
    def tearDown(self):
        if (self.driver != None):
            print("-----------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.quit()

    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        xpath = '//header[@class="page-header"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'unknow user unknow user'
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = 'changeme@test.test'
        user_pass = 'changeme-pass'
        driver = self.driver
        driver.get(self.login_url)
        functional_helpers.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_incorrect_login(self):
        # expected_text is a warning message about authentication failed
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@class="alert alert-danger"]'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver
        driver.get(self.login_url)
        functional_helpers.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)

    def test_check_product_name(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        driver = self.driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, name_xpath, expected_product_name)

    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        driver = self.driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, price_xpath, expected_product_price)

    def user_login(self, driver, user_email, user_pass):
        # finding login input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
        login_input_element.send_keys(user_email)
        # finding password input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
        login_input_element.send_keys(user_pass)
        # finding button 'SIGN IN' and clicking it
        button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
        button_next_element.click()

    def assert_element_text(self, driver, xpath, expected_text):
        driver = self.driver
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')


class LostHatFrontPageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'http://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver\chromedriver.exe")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_is_slider_existing(self):
        # slider = "//*[@id='carousel']"
        # try :
        #     slider
        #     print("To jest slider")
        # except NoSuchElementException :
        #     print("Brak slidera")

        slider_xpath = "//*[@id='carousel']"
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath(slider_xpath)

    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = "//*[@id='carousel']"
        driver = self.driver
        driver.get(self.base_url)
        slider_element = driver.find_element_by_xpath(slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        self.assertLess(expected_min_height, actual_slider_height,
                        f'Element height found by xpath{slider_xpath} 'f'on page {driver.current_url}'
                        f' is smaller than expected {expected_min_height} px')
        self.assertLess(expected_min_width, actual_slider_width,
                        f'Element width found by xpath {slider_xpath} on page {driver.current_url}'
                        f' is smaller than expected {expected_min_width}px')
