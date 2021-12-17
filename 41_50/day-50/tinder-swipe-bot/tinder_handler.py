import time

from selenium import webdriver


class TinderHandler:

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def sign_in_with_mobile_number(self, mob_no):
        self.driver.get('https://tinder.com/')
        time.sleep(5)
        sign_in_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
        sign_in_btn.click()
        time.sleep(5)
        mob_sign_in_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button')
        mob_sign_in_btn.click()
        time.sleep(45)
        mob_no_input = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/input')
        mob_no_input.send_keys(mob_no)
        mob_no_submit_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
        mob_no_submit_btn.click()
        pin = input('Enter the PIN:\n')
        pin_in_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[1]')
        pin_in_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[2]')
        pin_in_3 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[3]')
        pin_in_4 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[4]')
        pin_in_5 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[5]')
        pin_in_6 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[6]')
        pin_in_1.send_keys(pin[0])
        pin_in_2.send_keys(pin[1])
        pin_in_3.send_keys(pin[2])
        pin_in_4.send_keys(pin[3])
        pin_in_5.send_keys(pin[4])
        pin_in_6.send_keys(pin[5])
        pin_submit_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
        pin_submit_btn.click()
        pin = input('Enter the PIN:\n')
        pin_in_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[1]')
        pin_in_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[2]')
        pin_in_3 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[3]')
        pin_in_4 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[4]')
        pin_in_5 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[5]')
        pin_in_6 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/input[6]')
        pin_in_1.send_keys(pin[0])
        pin_in_2.send_keys(pin[1])
        pin_in_3.send_keys(pin[2])
        pin_in_4.send_keys(pin[3])
        pin_in_5.send_keys(pin[4])
        pin_in_6.send_keys(pin[5])
        pin_submit_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
        pin_submit_btn.click()
        self.init_login()

    def init_login(self):
        time.sleep(5)
        allow_loc_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_loc_btn.click()
        time.sleep(5)
        not_int_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        not_int_btn.click()
        time.sleep(5)

    def swiper(self, right: bool):
        if right:
            btn = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
            btn.click()
        else:
            btn = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
            btn.click()

    def auto_swipe(self, like: bool, amount: int):
        i = 0
        while i < amount:
            i += 1
            time.sleep(3)
            self.swiper(like)

    def exit(self):
        time.sleep(10)
        self.driver.close()
