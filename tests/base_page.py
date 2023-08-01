from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = ''

    def maximize_window(self):
        self.driver.maximize_window()

    def get_url(self):
        self.driver.get(self.url)

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)

    def new_window(self):
        """Переключиться на новую вкладку"""
        new_window = self.driver.window_handles[1]
        return self.driver.switch_to.window(new_window)

    def get_current_url(self):
        get_current_url = self.driver.current_url
        return get_current_url

    def find_element(self, locator, timeout=5):
        """ Найти элемент' """

        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element
