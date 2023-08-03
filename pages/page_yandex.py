from pages.base_page import BasePage
from pages.locators import YaPageLocators


class YaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ya.ru/"

    def find_menu(self):
        """ Найти меню, требуется для нескольких функций"""
        element = self.find_webelement(YaPageLocators.locator_find_menu)
        return element

    def find_search_field(self):
        """ПОИСК 2 шаг Найти поле поиска, требуется для нескольких функций, в нескольких тестах"""
        element = self.find_webelement(YaPageLocators.locator_find_search_field)
        return element

    def text_tensor(self):
        """ПОИСК 3 шаг Ввести в поиск Тензор"""
        element = self.find_search_field().send_keys('Тензор')
        return element

    def suggest(self):
        """ПОИСК 4 шаг Проверить, что появилась таблица с подсказками (suggest)"""
        element = self.find_webelement(YaPageLocators.locator_suggest)
        return element

    def press_enter(self):
        """ПОИСК 5 шаг Нажать enter"""
        element = self.find_search_field().send_keys("\n")
        return element

    def check_menu(self):
        """PIC 2 шаг Проверка что меню присутствует на странице"""
        self.find_menu()
        print("Сначала кнопка меню не найдена, так как она становится видна после клика в поле поиска")
        # клик по полю поиска, чтобы появилось быстрое меню
        self.find_search_field().click()
        # Повторно проверяем, что кнопка меню присутствует на странице
        self.find_menu()

    def go_to_pictures(self):
        """PIC 3 шаг Открыть меню, выбрать картинки"""
        # Открыть меню
        self.find_menu().click()
        # Выбрать картинки
        self.find_webelement(YaPageLocators.locator_choose_pictures).click()
        # переключиться на открывшуюся вкладку
        self.new_window()

    def check_images_url(self):
        """PIC 4 шаг Проверка, что перешли на страницу https://ya.ru/images/"""
        expected_url = 'https://ya.ru/images/'
        current_url = self.get_current_url()
        assert current_url == expected_url, "Мы не перешли на url https://ya.ru/images/"