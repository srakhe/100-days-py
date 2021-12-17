from selenium import webdriver
import time


class FormDataHandler:

    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path='/path/to/geckodriver')
        self.url = 'https://forms.gle/uE98dL359D2bdvUL6'

    def submit_form(self, price, address, link):
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(5)
        price_input = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price)
        address_input.send_keys(address)
        link_input.send_keys(link)
        submit_btn = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit_btn.click()
