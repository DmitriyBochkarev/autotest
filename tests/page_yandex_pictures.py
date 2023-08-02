from tests.base_page import BasePage
from tests.locators import YaPicturesPageLocators


class YaPicturesPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

    def pic_name(self):
        """Получить название картинки, требуется для нескольких функций"""
        element = self.find_webelement(YaPicturesPageLocators.locator_pic_name)
        return element

    def check_images_url(self):
        """PIC 4 шаг Проверка, что перешли на страницу https://yandex.ru/images/"""
        expected_url = 'https://yandex.ru/images/'
        current_url = self.get_current_url()
        assert current_url == expected_url, "Мы не перешли на url https://yandex.ru/images/"

    def first_pic_category_click(self):
        """PIC 5 шаг Открыть первую категорию"""
        global first_category_name
        first_category_name = self.find_webelement(YaPicturesPageLocators.locator_first_pic_category).get_attribute(
            'data-grid-text')
        element = self.find_webelement(YaPicturesPageLocators.locator_first_pic_category).click()
        return element

    def check_text_search_field(self):
        """PIC 6 шаг Проверка, что в поле поиска картинок отображается название категории"""
        element_get_content = self.find_webelement(YaPicturesPageLocators.locator_text_search_field).get_attribute(
            'value')
        assert first_category_name == element_get_content, "Названия первой категории нет в поле поиска"

    def first_pic_click(self):
        """PIC 7 шаг Первая картинка"""
        element = self.find_webelement(YaPicturesPageLocators.locator_first_pic).click()
        return element

    def pic_preview_check(self):
        """PIC 8 шаг Проверить что картинка открылась"""
        element = self.find_webelement(YaPicturesPageLocators.locator_pic_preview).is_displayed()
        assert element, "Картинка не открылась"
        # Запомним имя первой картинки для последующей проверки
        global first_pic_name
        first_pic_name = self.find_webelement(YaPicturesPageLocators.locator_pic_preview).get_attribute('src')

    def next_button_click(self):
        """PIC 9 шаг Кнопка вперед"""
        element = self.find_webelement(YaPicturesPageLocators.locator_next_button).click()
        return element

    def check_pic_change(self):
        """PIC 10 шаг Проверить что картинка сменилась"""
        second_pic_name = self.pic_name()
        assert second_pic_name != first_pic_name, "Картинка не сменилась"

    def prev_button_click(self):
        """PIC 11 шаг Кнопка назад"""
        element = self.find_webelement(YaPicturesPageLocators.locator_prev_button).click()
        return element

    def check_prev_pic(self):
        """PIC 12 шаг Проверяем, что картинка осталась из шага 8"""
        back_pic_name = self.pic_name().get_attribute('src')
        assert back_pic_name == first_pic_name, "Картинка не такая же, какая была первой"
