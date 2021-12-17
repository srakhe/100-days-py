import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

WAIT_TIMES = 10


class InstaBot:

    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path='/path/to/geckodriver')

    def login(self, username, password):
        self.driver.get('https://www.instagram.com/')
        time.sleep(WAIT_TIMES)
        uname_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        uname_input.send_keys(username)
        pass_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        pass_input.send_keys(password)
        login_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        login_btn.click()
        time.sleep(WAIT_TIMES)
        dont_save_info_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        dont_save_info_btn.click()
        time.sleep(WAIT_TIMES)
        no_notifs_btn = None
        try:
            no_notifs_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        except NoSuchElementException:
            no_notifs_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        finally:
            no_notifs_btn.click()
        time.sleep(WAIT_TIMES)

    def search(self, username):
        time.sleep(WAIT_TIMES)
        search_box = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys(username)
        search_box.send_keys(Keys.ENTER)
        time.sleep(WAIT_TIMES)
        first_result = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]')
        first_result.click()
        time.sleep(WAIT_TIMES)

    def get_followers(self, count):
        followers_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()
        time.sleep(WAIT_TIMES)
        first_run = True
        total = 0
        for iters in range(1, count):
            for i in range(2, 6):
                total += 1
                if first_run:
                    followers_btn_list = self.driver.find_element_by_xpath(
                        f'/html/body/div[5]/div/div/div[2]/ul/div/li[{total}]/div/div[3]/button')
                else:
                    followers_btn_list = self.driver.find_element_by_xpath(
                        f'/html/body/div[5]/div/div/div[2]/ul/div/li[{total}]/div/div[2]/button')
                followers_btn_list.click()
                time.sleep(2)
            first_run = False
            scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(5)

    def quit(self):
        time.sleep(10)
        self.driver.close()
