# autotest 1.2
### Программа предназначена для автоматизированного тестирования сайта ya.ru
# Для запуска из командной строки на windows:
### Открыть командную строку и создать папку проекта
### Установить виртуальное окружение
```commandline
python -m venv venv_autotest
venv_autotest\Scripts\activate.bat
pip install -r requirements.txt
```
### Скачать проект
```commandline
git init
git remote add origin  https://github.com/DmitriyBochkarev/autotest.git
git pull https://github.com/DmitriyBochkarev/autotest.git
```
### Скачать chromedriver.exe (версия 114.0.5735.90) 
https://chromedriver.chromium.org/downloads
### Добавить chromedriver.exe в папку проекта
### Запуск тестов из командной строки windows
```commandline
pytest -s
```
### Для выполнения тестов и создания html отчета:
```commandline
pytest --html=report.html --self-contained-html
```
### Можете посмотреть созданный отчет в папке проекта