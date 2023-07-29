import time
from selenium import webdriver # импортируем webdriver

# Зайти на https://ya.ru/
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
driver.get("https://ya.ru/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(3) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
# TODO Проверить наличие поля поиска

# Ввести в поиск Тензор
element_1 = driver.find_element_by_id("text") # объявляем переменную element_1, задаём ей значение селектора поля поиска
element_1.send_keys("Тензор") # команда send_keys("значение") – нужна для ввода информации в поле
# TODO Проверить, что появилась таблица с подсказками (suggest)

# Нажать enter
element_1.send_keys("\n") # команда send_keys("значение") – нужна для ввода информации в поле
# TODO Проверить, что появилась страница результатов поиска
# TODO Проверить 1 ссылка ведет на сайт tensor.ru

driver.quit()