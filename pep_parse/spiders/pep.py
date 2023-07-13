from urllib.parse import urljoin
import scrapy
from pep_parse.items import PepParseItem
from pep_parse.settings import allowed_domains, start_urls


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = allowed_domains
    start_urls = start_urls

    def parse(self, response):
        hrefs = response.xpath(
            '//section[@id="numerical-index"]'
        ).xpath('.//a[@class="pep reference internal"]')
        for href in hrefs.css('a::attr(href)').getall():
            pep_link = urljoin(start_urls[-1], href)
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
