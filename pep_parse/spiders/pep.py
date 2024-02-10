import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """
    Паук для сбора информации о PEP
    (Python Enhancement Proposals) с peps.python.org.
    """
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """
        Разбирает главную страницу для
        получения ссылок на отдельные страницы PEP.
        """
        all_pages = response.css(
            'section[id=numerical-index]').css('a[href^="pep-"]')
        for page_link in all_pages:
            yield response.follow(page_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Разбирает отдельную страницу PEP для извлечения необходимой информации.
        """
        page = response.css('section[id=pep-page-section]')
        h1_title = response.css('h1.page-title::text').get()
        data = {
            'number': int(page.css('li::text')[2].get().replace('PEP ', '')),
            'name': h1_title.partition('– ')[2],
            'status': response.css('dt:contains("Status") + dd ::text').get()
        }
        yield PepParseItem(data)
