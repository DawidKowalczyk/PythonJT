import unittest

from selenium import webdriver


class BaseTestClass(unittest.TestCase) :
    @classmethod
    def setUp(self) :
        self.base_url = 'http://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver\chromedriver.exe")

    @classmethod
    def tearDown(self) :
        self.driver.quit()