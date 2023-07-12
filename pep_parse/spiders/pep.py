import scrapy
from urllib.parse import urljoin
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        hrefs = response.xpath(
            '//section[@id="numerical-index"]'
        ).xpath('.//a[@class="pep reference internal"]')
        for href in hrefs.css('a::attr(href)').getall():
            pep_link = urljoin(self.start_urls[-1], href)
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        num_title = response.css('h1.page-title::text').get()
        number, title = num_title.split('–')
        status = response.xpath(
            '//*[@id="pep-content"]/dl/dd[2]/abbr/text()'
        ).get()
        data = {
            'number': number.strip().split()[-1],
            'name': title.strip(),
            'status': status
        }
        yield PepParseItem(data)
