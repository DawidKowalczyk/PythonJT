from selenium import webdriver
from selenium.webdriver.remote.command import Command

driver = webdriver.Chrome(
    executable_path=r"C:\Users\DKW\Downloads\webdrivers\chromedriver.exe")
driver.get('http://onet.pl')


def current_url(self):
    """
    Gets the URL of the current page.
    :Usage:
        driver.current_url
    """
    return self.execute(Command.GET_CURRENT_URL)['value']


print(driver.current_url)
