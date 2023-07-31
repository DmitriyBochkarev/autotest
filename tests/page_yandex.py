from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from termcolor import colored
from tests.base_page import BasePage

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class MainPage(WebDriver):

    def __init__(self, url):
        super().__init__()
        self.url = url


    options = Options()
    options.page_load_strategy = 'normal'
    options.binary_location = 'C:/chromedriver.exe'
    driver = webdriver.Chrome(options=options)

    def search_field(self):
        """Поле поиска"""
        search_field = self.driver.find_element(By.ID, "text")
        return search_field

    def menu(self):
        """Кнопка меню (все)"""
        menu = self.driver.find_element(By.LINK_TEXT, "Все")
        return menu

    def element_pic(self):
        """Кнопка Картинки"""
        element_pic = self.driver.find_element(By.LINK_TEXT, "Картинки")
        return element_pic

    def new_window(self):
        """Переключиться на новую вкладку"""
        new_window = self.driver.window_handles[1]
        current_window = self.driver.current_window_handle
        return self.driver.switch_to.window(new_window)

    def get_current_url(self):
        get_current_url = self.driver.current_url
        return get_current_url

    def category_name(self):
        """Название первой категории"""
        category_name = self.driver.find_element(By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        return category_name.get_attribute('data-grid-text')

    def first_pic_category(self):
        """Ссылка первой категории"""
        first_pic_category = self.driver.find_element(By.CLASS_NAME,
                                                      'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        return first_pic_category

    def pic_search_field(self):
        """Поле поиска в картинках"""
        pic_search_field = self.driver.find_element(By.CLASS_NAME, 'input__control.mini-suggest__input')
        return pic_search_field.get_attribute('value')

    def first_pic(self):
        """Первая картинка"""
        first_pic = self.driver.find_element(By.CLASS_NAME, 'serp-item_pos_0')
        return first_pic

    def pic_preview(self):
        pic_preview = self.driver.find_element(By.CLASS_NAME, 'MMImage-Preview')
        return pic_preview

    def pic_name(self):
        pic_name = self.driver.find_element(By.CLASS_NAME, 'MMImage-Preview').get_attribute('src')
        return pic_name

    def next_button(self):
        """Кнопка вперед"""
        next_button = self.driver.find_element(By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext')
        return next_button

    def prev_button(self):
        """Кнопка назад"""
        prev_button = self.driver.find_element(By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev')
        return prev_button

    def find_menu(self, timeout=10):
        """ Find element on the page. """

        element = None
        attr = {'link_text': 'Все'}
        locator = (str('link_text').replace('_', ' '), str(attr.get('link_text')))
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element
