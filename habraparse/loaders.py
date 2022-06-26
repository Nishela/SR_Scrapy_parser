from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


def clean_nickname(item: str):
    return item.strip().removeprefix('@')


class HabrAuthorLoader(ItemLoader):
    default_item_class = dict
    author_name_out = TakeFirst()
    nickname_out = TakeFirst()
    nickname_in = MapCompose(clean_nickname)
