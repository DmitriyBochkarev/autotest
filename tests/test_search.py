from tests.page_yandex import MainPage
from selenium import webdriver

page = MainPage(webdriver.Chrome(), "https://ya.ru/")
page.implicitly_wait(5)
page.maximize_window()
page.get_url()


def test_find_search_field():
    # Проверить наличие поля поиска
    page.find_search_field()

def test_send_tensor():
    # Ввести в поиск Тензор
    page.search_field().send_keys('Тензор')

def test_suggest():
    # Проверить, что появилась таблица с подсказками (suggest)
    page.suggest()

def test_enter():
    # Нажать enter
    page.search_field().send_keys("\n")

def test_search_results():
    # Проверить, что появилась страница результатов поиска
    label_results = page.search_results()
    assert label_results == 'Результаты поиска'

def test_first_result():
    # TODO Проверить 1 ссылка ведет на сайт tensor.ru
    first_url = page.first_url()
    assert first_url == 'https://tensor.ru/'


