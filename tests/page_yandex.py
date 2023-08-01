from selenium.webdriver.common.by import By

from tests.base_page import BasePage


class YaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ya.ru/"

    def element_pic(self):
        """Кнопка Картинки"""
        element = self.driver.find_element(By.LINK_TEXT, "Картинки")
        return element

    def category_name(self):
        """Название первой категории"""
        element = self.driver.find_element(By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        return element.get_attribute('data-grid-text')

    def first_pic_category(self):
        """Ссылка первой категории"""
        element = self.driver.find_element(By.CLASS_NAME,
                                           'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        return element

    def pic_search_field(self):
        """Поле поиска в картинках"""
        element = self.driver.find_element(By.CLASS_NAME, 'input__control.mini-suggest__input')
        return element.get_attribute('value')

    def first_pic(self):
        """Первая картинка"""
        element = self.driver.find_element(By.CLASS_NAME, 'serp-item_pos_0')
        return element

    def pic_preview(self):
        """Превью картинки"""
        element = self.driver.find_element(By.CLASS_NAME, 'MMImage-Preview')
        return element

    def pic_name(self):
        """Получить название первой картинки"""
        element = self.driver.find_element(By.CLASS_NAME, 'MMImage-Preview').get_attribute('src')
        return element

    def next_button(self):
        """Кнопка вперед"""
        element = self.driver.find_element(By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext')
        return element

    def prev_button(self):
        """Кнопка назад"""
        element = self.driver.find_element(By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev')
        return element

    def find_menu(self):
        """ Найти поле поиска """

        locator = (By.LINK_TEXT, 'Все')
        element = self.find_element(locator)
        return element

    def find_search_field(self):
        """ Найти поле поиска """

        locator = (By.ID, 'text')
        element = self.find_element(locator)
        return element

    def suggest(self):
        locator = (By.CLASS_NAME, 'mini-suggest__popup-content')
        element = self.find_element(locator)
        return element

    def search_results(self):
        """Результаты поиска"""
        locator = (By.CLASS_NAME, 'serp-list.serp-list_left_yes')
        element = self.find_element(locator)
        return element.get_attribute('aria-label')

    def first_url(self):
        """Ссылка на первый результат поиска"""
        element = self.driver.find_element(By.XPATH, '//li[@data-cid="0"]//a')
        return element.get_attribute('href')
