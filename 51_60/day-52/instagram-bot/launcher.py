from insta_bot import InstaBot
import os

INSTAGRAM_USERNAME = os.environ['INSTA_USERNAME']
INSTAGRAM_PASSWORD = os.environ['INSTA_PASSWORD']
COUNT_TO_FOLLOW = 50  # Factor of 5
ACCOUNT_TO_FOLLOW = 'instagram'

instaBot = InstaBot()
instaBot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
instaBot.search(username=ACCOUNT_TO_FOLLOW)
instaBot.get_followers(COUNT_TO_FOLLOW // 5)
