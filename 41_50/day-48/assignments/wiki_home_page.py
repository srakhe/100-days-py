import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox_driver = '/path/to/geckodriver'
driver = webdriver.Firefox(executable_path=firefox_driver)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
article_count_link = driver.find_element_by_css_selector('#articlecount a')
print(article_count_link.text)
article_count_link.click()

driver.back()

search = driver.find_element_by_name('search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()
