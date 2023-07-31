from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from termcolor import colored


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def maximize_window(self):
        self.driver.maximize_window()



    def get_url(self):
        self.driver.get(self.url)

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)
