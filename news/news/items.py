# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    website_name = scrapy.Field()
    category = scrapy.Field()
    language  = scrapy.Field()
    authors = scrapy.Field()
    published_date = scrapy.Field()