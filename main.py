import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
LOGIN = os.getenv('LOGIN')
SIMILAR_ACC = 0


driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=driver_options)

driver.get('https://www.instagram.com/')
time.sleep(1)
# click on cookies popup
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
#login and password
driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys(LOGIN)
driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys(PASSWORD, Keys.ENTER)
#wait for email code to be entered by user
time.sleep(30)
