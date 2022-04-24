import scrapy


class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['http://habr.com/']

    def parse(self, response):
        article_links = response.css('article h2.tm-article-snippet__title a')
        pagination = response.css('div.tm-pagination a.tm-pagination__page')
        for link in pagination:
            yield response.follow(link.attrib.get('href', None), callback=self.parse)
        for link in article_links:
            yield response.follow(link.attrib.get('href', None), callback=self.article_parse)

    def article_parse(self, response):
        author_data = response.css('div.tm-article-snippet__meta span.tm-user-info a.tm-user-info__username')
        yield response.follow(author_data[0].attrib.get('href', None), callback=self.author_parse)

    def author_parse(self, response):
        print(1)
        yield {'a': 1, 'b': 2}
