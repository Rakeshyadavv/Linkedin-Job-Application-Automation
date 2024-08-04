"""
Project : Automate the task of job apply on linkdin.
Developer : Rakesh Yadav
Date : 20-04-2024

"""

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
import os

def setup_logger():
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the logging level
    logpath = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(logpath, 'linkedin_job_apply_log.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler and set the logging level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and set the format for the log entries
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

log = setup_logger()

# close page function
def close_page():
    log.info("Inside function cloge_page")
    time.sleep(3)
    close_button = driver.find_element(By.XPATH, value="//button[@aria-label='Dismiss']")   
    close_button.click()
    time.sleep(2)
    log.info("Discarding the job")
    # save_button = driver.find_element(By.XPATH, value='//button[@data-control-name="save_application_btn"]')
    # save_button.click()
    discard_button = driver.find_element(By.XPATH, value='//button[@data-control-name="discard_application_confirm_btn"]')
    discard_button.click()
    log.info("Job discarded successfully")
    

# Job apply function
def Linkedin_Job_Apply():
    try:

        account_email = "Your linkedin email id"
        account_password = "Your linkedin password"
        url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

        chrome_options = webdriver.ChromeOptions()
        log.info(chrome_options)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=chrome_options)
        log.info(driver)

        log.info("Started")
        driver.maximize_window()
        driver.delete_all_cookies()
        time.sleep(1)
        log.info(f"Opening browser with url : {url}")
        driver.get(url)

        #Input account mail
        time.sleep(1)
        username = driver.find_element(By.ID,value="username")
        username.send_keys(account_email)
        log.info(f"entring username : {account_email}")

        #Input account password
        time.sleep(1)
        password = driver.find_element(By.ID, value="password")
        password.send_keys(account_password)
        log.info(f"entring password : {account_password}")

        #Click enter
        time.sleep(1)
        submit = driver.find_element(By.CLASS_NAME,value="login__form_action_container")
        submit.click()

        time.sleep(1)

        # log.info("wrong cred line")
        # wrong_credentials = driver.find_element(By.ID , value="error-for-password")
        # log.info(f"Wrong Credentials:  {wrong_credentials}")


        # if wrong_credentials:
        #     log.info("Wrong email or password. Try again or create an account")
        #     time.sleep(3)
        #     driver.quit()
        #else:
        log.info("Press Enter when you have solved the Captcha")
        # If asking for captcha solving, otherwise comment this line
        #input("Press Enter when you have solved the Captcha")

        #click on job menu
        time.sleep(2)
        jobs = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a/span')
        jobs.click()

        time.sleep(10)
        show_all = driver.find_element(By.CSS_SELECTOR,value='a.app-aware-link.discovery-templates-jobs-home-vertical-list__footer')
        show_all.click()

        time.sleep(15)
        all_jobs = driver.find_elements(By.CSS_SELECTOR,"li.ember-view.jobs-search-results__list-item")
        #all_jobs = driver.find_elements(By.CSS_SELECTOR, "li.discovery-templates-entity-item")
        log.info(f"Total jobs searched : {len(all_jobs)}")
        #print(len(all_jobs))
        time.sleep(5)
        counter = 0
        for item in all_jobs:
            counter +=1
            log.info(f"Applying for {counter} job :")
            item.click()
            time.sleep(3)

            try:
        
                easy_apply = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button")
                log.info(f"Applying via {easy_apply.text} " )
                #print(easy_apply.text)  
                easy_apply.click()

                time.sleep(4)
                close_page()

                
                    
                # submit_application= driver.find_element(By.CSS_SELECTOR,value=".artdeco-button__text")
                #     #submit_application = driver.find_element(By.XPATH, value="//button[@aria-label='Submit application']")
                # print(submit_application.text)
                    # if submit_application:
                    #     submit_application.click()
                    # else:
                    #     time.sleep(2)
                    #     close_page()
                        # submit_button = driver.find_element(By.XPATH, value="//button[@aria-label='Continue to next step']")
                        # print(submit_button.text)

                        # time.sleep(5)
                
            except Exception as e:
                log.error(f'Error: %s',e)
                continue
        log.info(f"Total jobs applied or discarded is : {counter}")
        #print(counter)
        time.sleep(10)
        driver.quit()
    except Exception as e:
        log.error(f'Error: %s',e)
        time.sleep(10)
        driver.quit()

if __name__ == '__main__':
    log.info('Inside Main Function')
    Linkedin_Job_Apply()





 



