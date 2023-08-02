from tests.base_page import BasePage
from tests.locators import YaSearchLocators


class YaSearchPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

    def check_search_results(self):
        """ПОИСК 6 шаг Проверить, что появилась страница результатов поиска"""
        element = self.find_webelement(YaSearchLocators.locator_check_search_results).get_attribute('aria-label')
        assert element == 'Результаты поиска', "Страница результатов поиска не открылась"

    def check_first_url(self):
        """ПОИСК 7 шаг Проверить 1 ссылка ведет на сайт tensor.ru"""
        element = self.find_webelement(YaSearchLocators.locator_check_first_url).get_attribute('href')
        assert element == 'https://tensor.ru/', "Первая ссылка ведет не на Тензор"
