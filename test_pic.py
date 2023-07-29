import time
from selenium import webdriver # импортируем webdriver

print("Зайти на ya.ru") # Зайти на ya.ru
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
driver.get("https://ya.ru/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(3) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
# TODO Проверить, что кнопка меню присутствует на странице

print("Открыть меню, выбрать Картинки")# Открыть меню, выбрать “Картинки”
element_1 = driver.find_element_by_id("text") # объявляем переменную element_1, задаём ей значение селектора поля поиска
element_1.click()
time.sleep(3)
element_all = driver.find_element_by_link_text("Все")
element_all.click()
time.sleep(3)
element_pic = driver.find_element_by_link_text("Картинки")
element_pic.click() # открывается в новой вкладке
time.sleep(3)
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
print("Проверить, что перешли на url https://yandex.ru/images/")# Проверить, что перешли на url https://yandex.ru/images/
link = driver.current_url
assert link == 'https://yandex.ru/images/'
print("Мы перешли на " + link)

time.sleep(5) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
print("получим название 1 категории")# получим название 1 категории
category = driver.find_element_by_class_name('PopularRequestList-SearchText')
category_get_text = category.text
print("Название 1 категории: " + category_get_text)

print("Открыть первую категорию") # Открыть первую категорию
pic_category = driver.find_element_by_class_name('PopularRequestList-Item.PopularRequestList-Item_pos_0')
pic_category.click()
time.sleep(3)
print("Проверить, что название категории отображается в поле поиска")# Проверить, что название категории отображается в поле поиска
element = driver.find_element_by_name("description") # нашли элемент
element_get_content = element.get_attribute('content') # получили текст атрибута content с помощью get_attribute
print("Текст в поле поиска: " + element_get_content)
print("Название категории: " + category_get_text)
assert category_get_text in element_get_content # добавили проверку что название 1 категории есть в атрибуте content (в поле поиска)

print("Открыть 1 картинку") # Открыть 1 картинку
pic = driver.find_element_by_class_name('serp-item_pos_0')
pic.click()
time.sleep(3)
# TODO Проверить, что картинка открылась

print("Нажать кнопку вперед") # Нажать кнопку вперед
next_button = driver.find_element_by_class_name('MediaViewer_theme_fiji-ButtonNext')
next_button.click()
time.sleep(3)
# TODO Проверить, что картинка сменилась

print("Нажать кнопку назад") # Нажать назад
prev_button = driver.find_element_by_class_name('MediaViewer_theme_fiji-ButtonPrev')
prev_button.click()
time.sleep(3)
# TODO Проверить, что картинка осталась из шага 8
driver.quit()
