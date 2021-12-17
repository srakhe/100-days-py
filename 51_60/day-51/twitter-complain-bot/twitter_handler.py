import time

from selenium import webdriver


class TwitterHandler:

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def log_in_with_email_and_password(self, email, password):
        self.driver.get('https://twitter.com/?lang=en')
        time.sleep(5)
        log_in_btn = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        log_in_btn.click()
        time.sleep(5)
        email_input = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pass_input.send_keys(password)
        time.sleep(2)
        log_in_submit_btn = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        log_in_submit_btn.click()

    def write_tweet(self, tweet_content):
        time.sleep(10)
        tweet_input = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_input.click()
        time.sleep(3)
        tweet_input.send_keys(tweet_content)
        print(tweet_content)
        time.sleep(10)
        send_tweet_btn = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        send_tweet_btn.click()

    def exit(self):
        time.sleep(10)
        self.driver.close()
