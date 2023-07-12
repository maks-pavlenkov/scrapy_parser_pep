# Проект парсинга сайта python

Проект выполняет парсинг всех известных PEP c оф сайта Python
- cобирает информацию обо всех pep
- cоздает 2 csv файла с результатами

### Как запустить проект:

- Клонировать репозиторий:

```
git clone https://github.com/maks-pavlenkov/scrapy_parser_pep.git
```
- Перейти в директорию и создать виртуальное окружение командой python3 -m venv venv
- Активировать виртуальное окружение командой - source venv/bin/activate
- Установить все зависимости командой - pip install -r requirements.txt
- Проект готов, запустить одну из функций

### Запуск
scrapy crawl pep

### CSV файлы
Создается два файла 
- 1ый с полями - number,name,status. Список всех Pep
- 2ой сводный - группировка Pep по статусам и их итоговое количество
#### Пример первого csv

| Number | Name                                | Status      |
|--------|:------------------------------------|:------------|
| 237    | Unifying Long Integers and Integers |  Final      |
| 229    | Using Distutils to Build Python     | Final       |
| 1      | PEP Purpose and Guidelines          | Active      |


#### Пример второго csv

| Статус     | Количество |
|------------|:------------|
| Active     | 62         |
| Withdrawn  | 56         |
| Final      | 273        |
| Superseded | 20         |
| Rejected   | 122        |
| Deferred   | 37         |
| Accepted   | 49         |
| Draft      | 25         |
| Total      | 644        |
