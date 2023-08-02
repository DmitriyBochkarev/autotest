from tests.page_yandex import YaPage


class TestSearch:
    def test_search(self, web_browser):
        # 1) Зайти на https://ya.ru/
        page = YaPage(web_browser)
        page.get_url()

        # 2) Проверить наличие поля поиска
        page.find_search_field()

        # 3) Ввести в поиск Тензор
        page.text_tensor()

        # 4) Проверить, что появилась таблица с подсказками (suggest)
        page.suggest()

        # 5) Нажать enter
        page.press_enter()

        # 6) Проверить, что появилась страница результатов поиска
        page.check_search_results()

        # 7) Проверить 1 ссылка ведет на сайт tensor.ru
        page.check_first_url()
