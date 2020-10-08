import datetime
import unittest
from selenium import webdriver
from wtguitesting.locators import xpath


class LostHatTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\DKW\Downloads\webdrivers\chromedriver.exe")

    @classmethod
    def tearDown(self):
        if (self.driver != None):
            print("-----------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.quit()
        self.driver.close()

    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        driver = self.driver
        driver.get(self.login_url)
        header_element = driver.find_element_by_xpath('//header[@class="page-header"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def test_correct_login(self):
        expected_text = 'unknow user unknow user'
        user_email = 'changeme-email@test.test'
        user_pass = 'changeme_password'
        driver = self.driver

        driver.get(self.login_url)
        # finding login input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
        login_input_element.send_keys(user_email)
        # finding password input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
        login_input_element.send_keys(user_pass)
        # finding button 'sign in'
        button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
        button_next_element.click()
        header_element = driver.find_element_by_xpath('//a[@class="account"]/*[@class="hidden-sm-down"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected title differ from actual title for page url: {self.login_url}')

    def test_check_product_name_and_price(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        expected_product_price = 'PLN23.52'
        driver = self.driver
        driver.get(self.sample_product_url)
        name_element = driver.find_element_by_xpath('//*[@class="col-md-6"]//*[@itemprop="name"]')
        name_element_text = name_element.text
        self.assertEqual(expected_product_name, name_element_text,
                         f'Expected text differ from actual for page url: {self.sample_product_url}')
        price_element = driver.find_element_by_xpath('//*[@class="current-price"]//*[@itemprop="price"]')
        price_element_text = price_element.text
        self.assertEqual(expected_product_price, price_element_text,
                         f'Expected text differ from actual for page url: {self.sample_product_url}')

    def user_login(self, driver, user_email, user_pass):
        login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
        login_input_element.send_keys(user_email)

        login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
        login_input_element.send_keys(user_pass)

        button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
        button_next_element.click()


    def test_correct_login(self):
        expected_text = 'changeme-username changeme-usersurname'
        user_email = 'changeme@test.test'
        user_pass = 'changeme-pass'

        driver = self.driver
        driver.get(self.login_url)
        self.user_login(driver, user_email, user_pass)

        header_element = driver.find_element_by_xpath('//a[@class="account"]/*[@class="hidden-sm-down"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def test_incorrect_login(self):
        # expected_text is a warning message about authentication failed
        expected_text = 'Authentication failed.'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver
        driver.get(self.login_url)
        self.user_login(driver, user_email, user_pass)
        alert_element = driver.find_element_by_xpath('//*[@class="alert alert-danger"]')
        alert_element_text = alert_element.text
        self.assertEqual(expected_text, alert_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def assert_element_text(self, driver, xpath, expected_text):
        header_element = driver.find_element_by_xpath(xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual on page: {driver.current_url}')


    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')

    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        xpath = '//header[@class="page-header"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'changeme-username changeme-usersurname'
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = 'changeme@test.test'
        user_pass = 'changeme-pass'
        driver = self.driver
        driver.get(self.login_url)
        self.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_incorrect_login(self):
        # expected_text is a warning message about authentication failed
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@class="alert alert-danger"]'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver
        driver.get(self.login_url)
        self.user_login(driver, user_email, user_pass)
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
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')

    def test_incorrect_login(self):
        # expected_text is a warning message about authentication failed
        expected_text = 'Authentication failed.'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver
        driver.get(self.login_url)

        self.login(user_email, user_pass)
        button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
        button_next_element.click()

        alert_element = driver.find_element_by_xpath('//*[@class="alert alert-danger"]')
        alert_element_text = alert_element.text
        self.assertEqual(expected_text, alert_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def login(self, driver, user_mail, user_pass):
        expected_text = 'Authentication failed.'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver
        login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
        login_input_element.send_keys(user_mail)
        # finding password input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
        login_input_element.send_keys(user_pass)

    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'changeme-username changeme-usersurname'
        user_email = 'changeme@test.test'
        user_pass = 'changeme-pass'

        driver = self.driver
        driver.get(self.login_url)
        self.user_login(driver, user_email, user_pass)

        self.assert_element_text(driver, xpath, expected_text)
        header_element = driver.find_element_by_xpath(xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page: {driver.current_url}')
