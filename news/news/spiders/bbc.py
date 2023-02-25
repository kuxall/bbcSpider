import scrapy
from news.items import NewsItem

class BbcSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["http://www.bbc.com/nepali"]

    def parse(self, response):
        item = NewsItem()
        for links in response.css('h3.bbc-150hhyj'):  
            item['link'] = "https://www.bbc.com" + links.css('a::attr(href)').get()
            print(item['link'])
            yield scrapy.Request(item['link'], callback=self.parse_details)
                        
    def parse_details(self, response):
        item = NewsItem()
        item['link'] = response.url
        item['summaries'] = response.css('b::text').getall()
        item['text'] = response.css('p::text ').getall()
        yield item
