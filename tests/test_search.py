from tests.page_yandex import YaPage


class TestSearch:
    def test_search(self, web_browser):
        # 1) Зайти на https://ya.ru/
        page = YaPage(web_browser)
        page.get_url()

        # 2) Проверить наличие поля поиска
        page.find_search_field()

        # 3) Ввести в поиск Тензор
        page.find_search_field().send_keys('Тензор')

        # 4) Проверить, что появилась таблица с подсказками (suggest)
        page.suggest()

        # 5) Нажать enter
        page.find_search_field().send_keys("\n")

        # 6) Проверить, что появилась страница результатов поиска
        label_results = page.search_results()
        assert label_results == 'Результаты поиска', "Страница результатов поиска не открылась"

        # 7) Проверить 1 ссылка ведет на сайт tensor.ru
        first_url = page.first_url()
        assert first_url == 'https://tensor.ru/', "Первая ссылка ведет не на Тензор"
