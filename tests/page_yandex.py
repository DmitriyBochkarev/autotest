from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:

    driver = webdriver.Chrome()
    driver.maximize_window()
    open_yandex = driver.get("https://ya.ru/")

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)

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
        first_pic_category = self.driver.find_element(By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        return first_pic_category

    def pic_search_field(self):
        """Поле поиска в картинках"""
        pic_search_field = self.driver.find_element(By.CLASS_NAME, 'input__control.mini-suggest__input')
        return pic_search_field.get_attribute('value')
        # return pic_search_field

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