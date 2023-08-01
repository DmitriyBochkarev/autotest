from selenium.webdriver.common.by import By

from tests.base_page import BasePage


class YaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ya.ru/"

    def element_pic(self):
        """Кнопка Картинки"""
        locator = (By.LINK_TEXT, "Картинки")
        element = self.find_webelement(locator)
        return element

    def category_name(self):
        """Название первой категории"""
        locator = (By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        element = self.find_webelement(locator)
        return element.get_attribute('data-grid-text')

    def first_pic_category(self):
        """Ссылка первой категории"""
        locator = (By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        element = self.find_webelement(locator)
        return element

    def pic_search_field(self):
        """Поле поиска в картинках"""
        locator = (By.CLASS_NAME, 'input__control.mini-suggest__input')
        element = self.find_webelement(locator)
        return element.get_attribute('value')

    def first_pic(self):
        """Первая картинка"""
        locator = (By.CLASS_NAME, 'serp-item_pos_0')
        element = self.find_webelement(locator)
        return element

    def pic_preview(self):
        """Превью картинки"""
        locator = (By.CLASS_NAME, 'MMImage-Preview')
        element = self.find_webelement(locator)
        return element

    def pic_name(self):
        """Получить название первой картинки"""
        locator = (By.CLASS_NAME, 'MMImage-Preview')
        element = self.find_webelement(locator).get_attribute('src')
        return element

    def next_button(self):
        """Кнопка вперед"""
        locator = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext')
        element = self.find_webelement(locator)
        return element

    def prev_button(self):
        """Кнопка назад"""
        locator = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev')
        element = self.find_webelement(locator)
        return element

    def find_menu(self):
        """ Найти меню """
        locator = (By.LINK_TEXT, 'Все')
        element = self.find_webelement(locator)
        return element

    def find_search_field(self):
        """ Найти поле поиска """
        locator = (By.ID, 'text')
        element = self.find_webelement(locator)
        return element

    def suggest(self):
        locator = (By.CLASS_NAME, 'mini-suggest__popup-content')
        element = self.find_webelement(locator)
        return element

    def search_results(self):
        """Результаты поиска"""
        locator = (By.CLASS_NAME, 'serp-list.serp-list_left_yes')
        element = self.find_webelement(locator)
        return element.get_attribute('aria-label')

    def first_url(self):
        """Ссылка на первый результат поиска"""
        locator = (By.XPATH, '//li[@data-cid="0"]//a')
        element = self.find_webelement(locator)
        return element.get_attribute('href')
