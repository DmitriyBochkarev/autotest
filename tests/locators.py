from selenium.webdriver.common.by import By


class YaPageLocators:
    locator_find_menu = (By.LINK_TEXT, 'Все')
    locator_find_search_field = (By.ID, 'text')
    locator_suggest = (By.CLASS_NAME, 'mini-suggest__popup-content')
    locator_check_search_results = (By.CLASS_NAME, 'serp-list.serp-list_left_yes')
    locator_check_first_url = (By.XPATH, '//li[@data-cid="0"]//a')
    locator_choose_pictures = (By.LINK_TEXT, "Картинки")


class YaPicturesPageLocators:
    locator_pic_name = (By.CLASS_NAME, 'MMImage-Preview')
    locator_first_pic_category = (By.CLASS_NAME, 'PopularRequestList-Item.PopularRequestList-Item_pos_0')
    locator_text_search_field = (By.CLASS_NAME, 'input__control.mini-suggest__input')
    locator_first_pic = (By.CLASS_NAME, 'serp-item_pos_0')
    locator_pic_preview = (By.CLASS_NAME, 'MMImage-Preview')
    locator_next_button = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext')
    locator_prev_button = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev')


class YaSearchLocators:
    locator_check_search_results = (By.CLASS_NAME, 'serp-list.serp-list_left_yes')
    locator_check_first_url = (By.XPATH, '//li[@data-cid="0"]//a')
    locator_choose_pictures = (By.LINK_TEXT, "Картинки")