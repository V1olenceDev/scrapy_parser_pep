import scrapy


class PepParseItem(scrapy.Item):
    """
    Класс для хранения информации о PEP.
    """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
