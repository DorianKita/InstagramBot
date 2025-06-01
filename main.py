import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
LOGIN = os.getenv('LOGIN')
SIMILAR_ACC = 'dirt_it_more'

class InstaFollower:
    def __init__(self):
        driver_options = webdriver.ChromeOptions()
        driver_options.add_experimental_option('detach', True)
        self.driver = driver = webdriver.Chrome(options=driver_options)



    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(5)
        # click on cookies popup
        self.driver.find_element(By.XPATH, "//*[text()='Odrzuć opcjonalne pliki cookie']").click()
        #login and password
        self.driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys(LOGIN)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys(PASSWORD, Keys.ENTER)
        #wait for email code to be entered by user
        time.sleep(7)

    def find_followers(self):
        time.sleep(5)
        # Show followers of the selected account.
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")

        time.sleep(3)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'obserwujących')]").click()
        time.sleep(3)
        modal = self.driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        # for i in range(10):
        #     # In this case we're executing some Javascript, that's what the execute_script() method does.
        #     # The method can accept the script as well as an HTML element.
        #     # The modal in this case, becomes the arguments[0] in the script.
        #     # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def follow(self):

        for element in self.driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]//button'):
            try:
                element.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                continue

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()