from tests.page_yandex import YaPage


class TestPic:
    def test_pic(self, web_browser):
        # 1) Зайти на ya.ru
        page = YaPage(web_browser)
        page.get_url()

        # 2) Проверить, что кнопка меню присутствует на странице
        page.find_menu()
        # клик по полю поиска, чтобы появилось быстрое меню
        page.find_search_field().click()
        # Повторно проверяем, что кнопка меню присутствует на странице
        page.find_menu()

        # 3) Открыть меню
        page.find_menu().click()
        # Выбрать картинки
        page.element_pic().click()
        # переключиться на открывшуюся вкладку
        page.new_window()

        # 4) Проверить, что перешли на url https://yandex.ru/images/
        expected_url = 'https://yandex.ru/images/'
        current_url = page.get_current_url()
        assert current_url == expected_url, "Мы не перешли на url https://yandex.ru/images/"

        # Получим название первой категории для последующей проверки
        first_category = page.category_name()

        # 5) Открыть первую категорию
        page.first_pic_category().click()

        #6) Проверить, что название категории отображается в поле поиска
        element_get_content = page.pic_search_field()
        assert first_category == element_get_content, "Названия первой категории нет в поле поиска"

        # 7) Открыть первую картинку
        page.first_pic().click()

        # 8) Проверить, что картинка открылась
        assert page.pic_preview().is_displayed(), "Картинка не открылась"

        # Запомним имя первой картинки для последующей проверки
        first_pic_name = page.pic_name()

        # 9) Нажать кнопку вперед
        page.next_button().click()

        # 10) Проверить, что картинка сменилась
        second_pic_name = page.pic_name()
        assert second_pic_name != first_pic_name, "Картинка не сменилась"

        # 11) Нажать назад
        page.prev_button().click()

        # 12) Проверяем, что картинка осталась из шага 8
        back_pic_name = page.pic_name()
        assert back_pic_name == first_pic_name, "Картинка не такая же, какая была первой"
