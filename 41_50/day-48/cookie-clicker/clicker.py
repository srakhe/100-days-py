from selenium import webdriver
import time

firefox_driver = '/path/to/geckodriver'
driver = webdriver.Firefox(executable_path=firefox_driver)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')


def upgrade():
    money_div = driver.find_element_by_id('money')
    money = int(money_div.text)
    store_div = driver.find_elements_by_css_selector('#store b')
    for i in range(len(store_div) - 1, -1, -1):
        store_item = store_div[i]
        item_desc = store_item.text.split(' - ')
        if len(item_desc) > 1:
            item_cost = item_desc[1].replace(',', '')
            if int(item_cost) <= money:
                print(f'Buying {item_desc[0]}')
                store_item.click()
                return


while True:
    timeout = time.time() + 5
    while True:
        cookie.click()
        if time.time() > timeout:
            upgrade()
            break
