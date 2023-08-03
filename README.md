# autotest 1.2
### Программа предназначена для автоматизированного тестирования сайта ya.ru
# Для запуска из командной строки на windows:
### 1) Открыть командную строку и создать папку проекта
### 2) Установить виртуальное окружение
```commandline
python -m venv venv_autotest
venv_autotest\Scripts\activate.bat
pip install -r requirements.txt
```
### 3) Скачать проект
```commandline
git init
git remote add origin  https://github.com/DmitriyBochkarev/autotest.git
git pull https://github.com/DmitriyBochkarev/autotest.git
```
### 4) Скачать chromedriver.exe (версия 114.0.5735.90) 
### Достаточно, чтобы в версии браузера и драйвера совпали только первые 3 цифры
https://chromedriver.chromium.org/downloads
### 5) Добавить chromedriver.exe в папку проекта, из которой будете запускать тесты
### 6) Запуск тестов из командной строки windows
```commandline
python -m pytest -s
```
## Для выполнения тестов и создания html отчета команда:
```commandline
pytest --html=report.html --self-contained-html
```
### Можете посмотреть созданный отчет в папке проекта

## Для логирования с помощью allure:
### 1) Создать папку для хранения результатов тестов
### 2) Запустить тесты командой:
```commandline
pytest --alluredir=/path/to/my_allure_reports
```
### 3) Собрать репорт командой:
```commandline
allure serve /path/to/my_allure_reports
```