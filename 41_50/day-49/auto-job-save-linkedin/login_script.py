from selenium import webdriver


def login(driver: webdriver.Firefox, email, password):
    print('Starting login..')
    driver.get('http://www.linkedin.com')
    email_input = driver.find_element_by_name('session_key')
    pass_input = driver.find_element_by_name('session_password')
    submit = driver.find_element_by_class_name('sign-in-form__submit-button')
    email_input.send_keys(str(email))
    pass_input.send_keys(str(password))
    submit.click()
    print('Login Completed')
