from tests.page_yandex import MainPage
from selenium import webdriver

page = MainPage(webdriver.Chrome(), "https://ya.ru/")
page.implicitly_wait(5)
page.get_url()
page.maximize_window()

# переменные для проверок
first_category = ""
first_pic_name = ""
second_pic_name = ""
back_pic_name = ""


def test_search_field_click():
    """клик по полю поиска, чтобы появилось быстрое меню"""

    # Проверить, что кнопка меню присутствует на странице

    page.search_field().click()  # клик по полю поиска, чтобы появилось быстрое меню
    page.find_menu()


def test_menu_click():
    """клик на кнопку меню"""
    assert page.menu().is_displayed(), "Кнопка меню присутствует на первоначальной странице"
    page.menu().click()


def test_element_pic_click():
    """клик на кнопку картинки"""
    page.element_pic().click()  # клик на кнопку картинки, открывается в новой вкладке
    page.new_window()

    # Проверить, что перешли на url https://yandex.ru/images/
    expected_url = 'https://yandex.ru/images/'
    current_url = page.get_current_url()
    assert current_url == expected_url

    global first_category
    first_category = page.category_name()  # получили название первой категории

    page.first_pic_category().click()

    element_get_content = page.pic_search_field()  # получили текст из поисковой строки
    assert first_category == element_get_content  # добавили проверку что название 1 категории есть в в поле поиска


def test_first_pic_click():
    """клик на первую картинку"""
    page.first_pic().click()
    # Проверяем, что картинка открылась
    assert page.pic_preview().is_displayed()

    # запомним имя первой картинки
    global first_pic_name
    first_pic_name = page.pic_name()


def test_next_button_click():
    """клик на кнопку далее"""
    page.next_button().click()

    # запомним имя второй картинки
    global second_pic_name
    second_pic_name = page.pic_name()
    # Проверяем, что картинка сменилась
    assert second_pic_name != first_pic_name


def test_prev_button_click():
    """клик на кнопку назад"""
    page.prev_button().click()

    # запомним имя картинки после возврата
    global back_pic_name
    back_pic_name = page.pic_name()
    # # Проверяем, что картинка осталась из шага 8
    assert back_pic_name == first_pic_name
