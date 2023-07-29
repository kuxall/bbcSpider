import scrapy
from news.items import NewsItem

class BbcSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["http://www.bbc.com/nepali"]

    def parse(self, response):
        for links in response.css('h3.bbc-150hhyj'):
            link = "https://www.bbc.com" + links.css('a::attr(href)').get()
            yield scrapy.Request(link, callback=self.parse_details)

    def parse_details(self, response):
        item = NewsItem()
        item['link'] = response.url

        summaries = response.css('b::text').getall()
        summaries = ' '.join(summaries)  # Join the summaries using a space separator
        summaries = summaries.replace(',', '')  # Remove commas from the concatenated summaries

        text = response.css('p::text').getall()
        text = ' '.join(text)  # Join the text using a space separator
        text = text.replace(',', '')  # Remove commas from the concatenated text

        # Concatenate summaries and text into a single field called 'summaries'
        item['summaries'] = summaries + text

        yield item
