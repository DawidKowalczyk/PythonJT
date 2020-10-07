import unittest

from selenium.webdriver.remote.command import Command
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

'selenium '

from helpers import operational_helpers as oh
from selenium import webdriver


class LostHatShoppingCartTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        self.driver = self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\DKW\Downloads\webdrivers\chromedriver.exe")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'

        driver = self.driver
        driver.get(self.subpage_art_url)

        item_element = driver.find_element_by_xpath(item_xpath)
        item_element.click()
        shopping_cart_button_element = driver.find_element_by_xpath(shopping_cart_button_xpath)
        shopping_cart_button_element.click()

        confirmation_modal_elements = oh.wait_for_elements(driver, confirmation_modal_title_xpath)
        confirmation_modal_element = confirmation_modal_elements[0]
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)

        element_lcated = EC.presence_of_element_located
        confirmation_modal_element = WebDriverWait(driver, 10).until(
            element_lcated((By.XPATH, confirmation_modal_title_xpath)))
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)

    @property
    def current_url(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        """
        Gets the URL of the current page.
        :Usage:
            driver.current_url
        """
        return self.execute(Command.GET_CURRENT_URL)['value']



