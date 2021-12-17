from selenium import webdriver
import time

firefox_driver = '/path/to/geckodriver'
driver = webdriver.Firefox(executable_path=firefox_driver)

driver.get('https://secure-retreat-92358.herokuapp.com/')
fname_input = driver.find_element_by_name('fName')
lname_input = driver.find_element_by_name('lName')
email_input = driver.find_element_by_name('email')
submit = driver.find_element_by_css_selector('.form-signin button')

fname_input.send_keys('Sherbert')
lname_input.send_keys('Ilama')
email_input.send_keys('sherbert@gmail.com')
submit.click()

time.sleep(5)
driver.close()
