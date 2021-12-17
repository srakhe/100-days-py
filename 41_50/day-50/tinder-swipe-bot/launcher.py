from selenium import webdriver
from tinder_handler import TinderHandler
import os

MOBILE_NUMBER = os.environ['MOBILE_NUMBER']
SWIPE_RIGHT = False
SWIPES_COUNT = 100

driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

tinderObj = TinderHandler(driver)
tinderObj.sign_in_with_mobile_number(MOBILE_NUMBER)
tinderObj.auto_swipe(SWIPE_RIGHT, SWIPES_COUNT)
tinderObj.exit()
