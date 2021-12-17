from selenium import webdriver
from twitter_handler import TwitterHandler
from internet_speed_handler import InternetSpeedHandler
import os

INTERNET_SPEED_WAIT_TIME = 2  # in minutes
COMPARE_DOWN_SPEED = 50  # in Mbps
COMPARE_UP_SPEED = 10  # in Mbps
INTERNET_PROVIDER = '@twitter'

TWITTER_EMAIL = os.environ['EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']

driver = webdriver.Firefox(
    executable_path='/path/to/geckodriver')

intSpeedObj = InternetSpeedHandler(driver, INTERNET_SPEED_WAIT_TIME)
twitterHandlerObj = TwitterHandler(driver)

down_speed, up_speed = intSpeedObj.get_speed()
if down_speed < COMPARE_DOWN_SPEED or up_speed < COMPARE_UP_SPEED:
    print('Speed is less than expected!')
    twitterHandlerObj.log_in_with_email_and_password(email=TWITTER_EMAIL, password=TWITTER_PASSWORD)
    twitterHandlerObj.write_tweet(
        f'Hi! {INTERNET_PROVIDER}, My internet speed is slow today!\nDown Speed expected: {COMPARE_DOWN_SPEED} Mbps, observed: {down_speed} Mbps, Up Speed expected: {COMPARE_UP_SPEED} Mbps, observed: {up_speed} Mbps.')
    twitterHandlerObj.exit()
else:
    print('No problems!')
