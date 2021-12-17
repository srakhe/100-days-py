import time
from selenium import webdriver


def get_jobs(driver: webdriver.Firefox, job_desc, job_loc):
    print('Going to job search page..')
    driver.get(f'https://www.linkedin.com/jobs/search/?f_AL=true&keywords={job_desc}&location={job_loc}')
    time.sleep(10)  # Wait for the jobs page to load
    jobs = driver.find_elements_by_css_selector('.artdeco-entity-lockup__title a')
    if jobs:
        print('Found jobs')
    return jobs


def save_job(driver: webdriver.Firefox, job: webdriver.Firefox.find_element_by_css_selector):
    print('Saving a job')
    job.click()
    save_btn = driver.find_element_by_class_name('jobs-save-button')
    time.sleep(5)  # Wait for job pane to load
    save_btn.click()
    print('Saved Job')
