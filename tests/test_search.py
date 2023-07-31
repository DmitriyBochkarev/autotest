from tests.page_yandex import MainPage
from selenium import webdriver


def test_search(web_browser):
    page = MainPage(webdriver.Chrome(), "https://ya.ru/")

    page.get_url()

    # Проверить наличие поля поиска
    page.find_search_field()

    # Ввести в поиск Тензор
    page.search_field().send_keys('Тензор')

    # Проверить, что появилась таблица с подсказками (suggest)
    page.suggest()

    # Нажать enter
    page.search_field().send_keys("\n")

    # Проверить, что появилась страница результатов поиска
    label_results = page.search_results()
    assert label_results == 'Результаты поиска', "Страница результатов поиска не открылась"

    # Проверить 1 ссылка ведет на сайт tensor.ru
    first_url = page.first_url()
    assert first_url == 'https://tensor.ru/', "Первая ссылка ведет не на Тензор"
