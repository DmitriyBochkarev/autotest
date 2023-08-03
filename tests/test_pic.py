from pages.page_yandex import YaPage
from pages.page_yandex_pictures import YaPicturesPage
from conftest import web_browser


class TestPic:
    def test_pic(self, web_browser):
        # 1) Зайти на ya.ru
        page = YaPage(web_browser)
        page.get_url()

        # 2) Проверить, что кнопка меню присутствует на странице
        page.check_menu()

        # 3) Открыть меню, выбрать картинки
        page.go_to_pictures()

        # 4) Проверить, что перешли на url https://yandex.ru/images/
        page.check_images_url()
        pictures_page = YaPicturesPage(web_browser, web_browser.current_url)

        # 5) Открыть первую категорию
        pictures_page.first_pic_category_click()

        # 6) Проверить, что название категории отображается в поле поиска
        pictures_page.check_text_search_field()

        # 7) Открыть первую картинку
        pictures_page.first_pic_click()

        # 8) Проверить, что картинка открылась
        pictures_page.pic_preview_check()

        # 9) Нажать кнопку вперед
        pictures_page.next_button_click()

        # 10) Проверить, что картинка сменилась
        pictures_page.check_pic_change()

        # 11) Нажать назад
        pictures_page.prev_button_click()

        # 12) Проверяем, что картинка осталась из шага 8
        pictures_page.check_prev_pic()
