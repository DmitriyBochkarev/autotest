from tests.page_yandex import MainPage


class TestPic:
    def test_pic(self, web_browser):
        page = MainPage(web_browser, "https://ya.ru/")
        page.get_url()

        # Проверить, что кнопка меню присутствует на странице
        page.find_menu()
        page.search_field().click()  # клик по полю поиска, чтобы появилось быстрое меню

        page.find_menu()

        # клик на кнопку меню
        page.menu().click()

        # клик на кнопку картинки
        page.element_pic().click()
        # переключиться на открывшуюся вкладку
        page.new_window()

        # Проверить, что перешли на url https://yandex.ru/images/
        expected_url = 'https://yandex.ru/images/'
        current_url = page.get_current_url()
        assert current_url == expected_url, "Мы не перешли на url https://yandex.ru/images/"

        first_category = page.category_name()  # получили название первой категории


        page.first_pic_category().click()
        # получим текст из поисковой строки
        element_get_content = page.pic_search_field()
        assert first_category == element_get_content, "Названия первой категории нет в поле поиска"

        # клик на первую картинку
        page.first_pic().click()
        # Проверяем, что картинка открылась
        assert page.pic_preview().is_displayed(), "Картинка не открылась"

        # запомним имя первой картинки
        first_pic_name = page.pic_name()

        # клик на кнопку далее
        page.next_button().click()

        # запомним имя второй картинки
        second_pic_name = page.pic_name()
        # Проверяем, что картинка сменилась
        assert second_pic_name != first_pic_name, "Картинка не сменилась"

        # клик на кнопку назад
        page.prev_button().click()

        # запомним имя картинки после возврата
        back_pic_name = page.pic_name()
        # Проверяем, что картинка осталась из шага 8
        assert back_pic_name == first_pic_name, "Картинка не такая же, какая была первой"
