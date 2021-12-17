from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import login_script
import jobs_manager
import os

LINKEDIN_EMAIL = os.environ['LINKEDIN_EMAIL']
LINKEDIN_PASS = os.environ['LINKEDIN_PASS']
JOB_DESC = 'Python'
LOCATION = 'Remote'

firefox_driver = '/path/to/geckodriver'
driver = webdriver.Firefox(executable_path=firefox_driver)
try:
    login_script.login(driver, LINKEDIN_EMAIL, LINKEDIN_PASS)
    jobs_list = jobs_manager.get_jobs(driver, JOB_DESC, LOCATION)
    count = 0
    for job in jobs_list:
        print(f'For job number: {count}')
        jobs_manager.save_job(driver, job)
        count += 1
except NoSuchElementException:
    print('There was a change in the HTML pattern of the website. Please update the code!')
else:
    print('Everything worked as expected')
finally:
    driver.quit()
