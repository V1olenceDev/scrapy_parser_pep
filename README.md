# Парсер Python.org

### Описание
Данный код представляет собой асинхронный парсер документации Python 
при помощи библиотеки **scrapy**. Он предоставляет возможность получить 
информацию о PEP (Python Enhancement Proposal) и их статусах.


### Инструкция по запуску:
Клонируйте репозиторий:
```commandline
git clone git@github.com:V1olenceDev/scrapy_parser_pep.git
```
Установите и активируйте виртуальное окружение:

```commandline
python -m venv venv
. venv/Scripts/activate
```

Установите зависимости из файла requirements.txt:
```commandline
pip install -r requirements.txt
```

### Использование:
Для запуска парсера необходимо перейти в папку pep_parse:
```commandline
cd pep_parse
```
И выполнить команду:
```commandline
scrapy crawl pep 
```
Результаты будут сохранены в папке results
- в файле pep_<date>.csv находится информация по всем PEP (их номер, название и статус)
- в файле status_summary_<date>.csv находится информация о колличестве статусов PEP


## Автор
[Гаспарян Валерий Гургенович](https://github.com/V1olenceDev)
