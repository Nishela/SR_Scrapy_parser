import scrapy
from ..loaders import HabrAuthorLoader


class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/']

    def parse(self, response):
        article_links = response.css('article h2.tm-article-snippet__title a')
        pagination = response.css('div.tm-pagination a.tm-pagination__page')
        for link in pagination:
            yield response.follow(link.attrib.get('href'), callback=self.parse)
        for link in article_links:
            yield response.follow(link.attrib.get('href'), callback=self.article_parse)

    def article_parse(self, response):
        data = {'url': response.url}
        author_data = response.css('div.tm-article-snippet__meta span.tm-user-info a.tm-user-info__username')
        yield response.follow(author_data[0].attrib.get('href', None), callback=self.author_parse, cb_kwargs=data)

    def author_parse(self, response, url):
        loader = HabrAuthorLoader(response=response)
        # TODO: спрятать в отдельный маппинг для каждого метода
        loader.add_xpath(
            'author_name',
            '//div[contains(@class,"tm-user-card__info")]//div[contains(@class,"tm-user-card__title")]/span/text()'
        )
        loader.add_xpath(
            'nickname',
            '//div[contains(@class,"tm-user-card__info")]//div[contains(@class,"tm-user-card__title")]/a/text()'
        )
        result = loader.load_item()
        print(1)
        # TODO: что такое item?
