import time
from selenium import webdriver


class InternetSpeedHandler:

    def __init__(self, driver: webdriver.Firefox, wait):
        self.driver = driver
        self.wait_time = wait

    def get_speed(self):
        url = 'https://www.speedtest.net/'
        self.driver.get(url)
        time.sleep(5)
        go_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        time.sleep(self.wait_time * 60)
        down_speed_label = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        down_speed = float(down_speed_label.text)
        up_speed_label = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        up_speed = float(up_speed_label.text)
        return down_speed, up_speed
