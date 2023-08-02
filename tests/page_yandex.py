from selenium.webdriver.common.by import By

from tests.base_page import BasePage


class YaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ya.ru/"

    def pic_name(self):
        """Получить название картинки, требуется для нескольких функций"""
        locator = (By.CLASS_NAME, 'MMImage-Preview')
        element = self.find_webelement(locator)
        return element

    def find_menu(self):
        """ Найти меню, требуется для нескольких функций"""
        locator = (By.LINK_TEXT, 'Все')
        element = self.find_webelement(locator)
        return element

    def find_search_field(self):
        """ПОИСК 2 шаг Найти поле поиска, требуется для нескольких функций, в нескольких тестах"""
        locator = (By.ID, 'text')
        element = self.find_webelement(locator)
        return element

    def text_tensor(self):
        """ПОИСК 3 шаг Ввести в поиск Тензор"""
        element = self.find_search_field().send_keys('Тензор')
        return element

    def suggest(self):
        """ПОИСК 4 шаг Проверить, что появилась таблица с подсказками (suggest)"""
        locator = (By.CLASS_NAME, 'mini-suggest__popup-content')
        element = self.find_webelement(locator)
        return element

    def press_enter(self):
        """ПОИСК 5 шаг Нажать enter"""
        element = self.find_search_field().send_keys("\n")
        return element

    def check_search_results(self):
        """ПОИСК 6 шаг Проверить, что появилась страница результатов поиска"""
        locator = (By.CLASS_NAME, 'serp-list.serp-list_left_yes')
        element = self.find_webelement(locator).get_attribute('aria-label')
        assert element == 'Результаты поиска', "Страница результатов поиска не открылась"

    def check_first_url(self):
        """ПОИСК 7 шаг Проверить 1 ссылка ведет на сайт tensor.ru"""
        locator = (By.XPATH, '//li[@data-cid="0"]//a')
        element = self.find_webelement(locator).get_attribute('href')
        assert element == 'https://tensor.ru/', "Первая ссылка ведет не на Тензор"

    def check_menu(self):
        """PIC 2 шаг Проверка что меню присутствует на странице"""
        self.find_menu()
        # клик по полю поиска, чтобы появилось быстрое меню
        self.find_search_field().click()
        # Повторно проверяем, что кнопка меню присутствует на странице
        self.find_menu()

    def go_to_pictures(self):
        """PIC 3 шаг Открыть меню, выбрать картинки"""
        # Открыть меню
        self.find_menu().click()
        # Выбрать картинки
        locator = (By.LINK_TEXT, "Картинки")
        element = self.find_webelement(locator).click()
        # переключиться на открывшуюся вкладку
        self.new_window()

    def check_images_url(self):
        """PIC 4 шаг Проверка, что перешли на страницу https://yandex.ru/images/"""
        expected_url = 'https://yandex.ru/images/'
        current_url = self.get_current_url()
        assert current_url == expected_url, "Мы не перешли на url https://yandex.ru/images/"

    def first_pic_category_click(self):
        """PIC 5 шаг Открыть первую категорию"""
        locator = (By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
        global first_category_name
        first_category_name = self.find_webelement(locator).get_attribute('data-grid-text')
        element = self.find_webelement(locator).click()
        return element

    def check_text_search_field(self):
        """PIC 6 шаг Проверка, что в поле поиска картинок отображается название категории"""
        locator = (By.CLASS_NAME, 'input__control.mini-suggest__input')
        element_get_content = self.find_webelement(locator).get_attribute('value')
        assert first_category_name == element_get_content, "Названия первой категории нет в поле поиска"

    def first_pic_click(self):
        """PIC 7 шаг Первая картинка"""
        locator = (By.CLASS_NAME, 'serp-item_pos_0')
        element = self.find_webelement(locator).click()

        return element

    def pic_preview_check(self):
        """PIC 8 шаг Проверить что картинка открылась"""
        locator = (By.CLASS_NAME, 'MMImage-Preview')
        element = self.find_webelement(locator).is_displayed()
        assert element, "Картинка не открылась"

        # Запомним имя первой картинки для последующей проверки
        global first_pic_name
        first_pic_name = self.find_webelement(locator).get_attribute('src')

    def next_button_click(self):
        """PIC 9 шаг Кнопка вперед"""
        locator = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext')
        element = self.find_webelement(locator).click()
        return element

    def check_pic_change(self):
        """PIC 10 шаг Проверить что картинка сменилась"""
        second_pic_name = self.pic_name()
        assert second_pic_name != first_pic_name, "Картинка не сменилась"

    def prev_button_click(self):
        """PIC 11 шаг Кнопка назад"""
        locator = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev')
        element = self.find_webelement(locator).click()
        return element

    def check_prev_pic(self):
        """PIC 12 шаг Проверяем, что картинка осталась из шага 8"""
        back_pic_name = self.pic_name().get_attribute('src')
        assert back_pic_name == first_pic_name, "Картинка не такая же, какая была первой"
