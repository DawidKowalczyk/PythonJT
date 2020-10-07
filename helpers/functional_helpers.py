
def user_login(driver, user_email, user_pass):
    # finding login input box and sending value
    login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
    login_input_element.send_keys(user_email)
    """
    Login to the page with correct credentials
    :param driver: webdriver instance
    :param user_mail: user mail
    :param user_password: user pwd
    :return: None
    """

    # finding password input box and sending value
    login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
    login_input_element.send_keys(user_pass)

    # finding button 'SIGN IN' and clicking it
    button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
    button_next_element.click()


