from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from habraparse.spiders.habr import HabrSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule('habraparse.settings')
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(HabrSpider)
    crawler_process.start()
