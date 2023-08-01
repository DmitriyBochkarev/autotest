# autotest
## Установка виртуального окружения
```commandline
pip install selenium
pip install pytest
pip install termcolor
pip install pytest-selenium
pip install pytest-html
```
## Добавить в папу проекта chromedriver.exe (версия 114.0.5735.90)
## Запуск тестов из командной строки windows
```commandline
pytest
```

### Для выполнения тестов и создания html отчета:
```commandline
pytest --html=report.html --self-contained-html
```