# Парсер Python.org

> Данный код представляет собой асинхронный парсер документации Python 
при помощи библиотеки **scrapy**. Он предоставляет возможность получить 
> информацию о PEP (Python Enhancement Proposal) и их статусах.

## Технологии проекта

- Python — высокоуровневый язык программирования.
- Scrapy — библиотека для веб-скрейпинга.
- Logging — Логирование работы и отслеживания ошибок.

### Как запустить проект:

Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:V1olenceDev/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```

```
. venv/Scripts/activate
```

Установите зависимости из файла `requirements.txt`:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните команду:
```commandline
scrapy crawl pep 
```
Результаты будут сохранены в папке results
- в файле `pep_<date>.csv` находится информация по всем PEP (их номер, название и статус)
- в файле `status_summary_<date>.csv` находится информация о колличестве статусов PEP


## Автор
[Гаспарян Валерий Гургенович](https://github.com/V1olenceDev)
