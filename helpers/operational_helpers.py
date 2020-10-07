import time


def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpath is greater than 0

           :param driver: webdriver instance
           :param xpath: xpath of web element
           :param max_seconds_to_wait: maximum waiting for element time
           :return: list of found elements
           :param max_seconds_to_wait:maximum time in seconds to wait for element(default: 5)
           :return: list of found elements
        """
    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements_by_xpath(xpath)

        print(f'Total waiting {seconds}s')

        if len(elements) >= number_of_expected_elements:
            return elements

        if seconds == (max_seconds_to_wait - 1):
            print('End of wait')
            assert len(elements) > 0, f'Element for xpath {xpath} not found in time of {max_seconds_to_wait}s'
        time.sleep(1)
