import time
from tests.yandex import MainPage


page = MainPage()
first_category = ""
def test_search_field_click():
    """клик по полю поиска, чтобы появилось быстрое меню"""

    # TODO Проверить, что кнопка меню присутствует на странице
    
    time.sleep(5)
    page.search_field().click() # клик по полю поиска, чтобы появилось быстрое меню
    time.sleep(3)

def test_menu_click():
    """клик на кнопку меню"""
    page.menu().click()
    time.sleep(3)

def test_element_pic_click():
    """клик на кнопку картинки"""
    page.element_pic().click() # клик на кнопку картинки, открывается в новой вкладке
    time.sleep(3)

    page.new_window()

    # print("Проверить, что перешли на url https://yandex.ru/images/")# Проверить, что перешли на url https://yandex.ru/images/
    # link = driver.current_url
    # assert link == 'https://yandex.ru/images/'
    # print("Мы перешли на " + link)

    time.sleep(3)
    global first_category
    first_category = page.category() # получили название первой категории


    page.first_pic_category().click()
    time.sleep(5)

    element_get_content = page.pic_search_field() # получили текст атрибута content с помощью get_attribute
    time.sleep(5)
    assert first_category == element_get_content # добавили проверку что название 1 категории есть в атрибуте content (в поле поиска)

def test_first_pic_click():
    """клик на первую картинку"""
    page.first_pic().click()
    time.sleep(3)
    # TODO Проверить, что картинка открылась
def test_next_button_click():
    """клик на кнопку далее"""
    page.next_button().click()
    time.sleep(3)
    # TODO Проверить, что картинка сменилась
def test_prev_button_click():
    """клик на кнопку назад"""
    page.prev_button().click()
    time.sleep(3)
    # TODO Проверить, что картинка осталась из шага 8

