import scrapy
import datetime
from news.items import NewsItem

class BbcSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["http://www.bbc.com/nepali"]

    def parse(self, response):
        for URLs in response.css('h3.bbc-150hhyj'):
            url = "https://www.bbc.com" + URLs.css('a::attr(href)').get()
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        item = NewsItem()
        item['url'] = response.url

        # Set published_date to the current date
        item['published_date'] = datetime.datetime.now().strftime("%Y-%m-%d")

        # Extract category from the url
        
        item['category'] = "politics"

        item['website_name'] = "BBC"


        item['authors'] = 'unknown'

        item['language'] = "nepali"

        title = response.css('b::text').getall()
        title = ' '.join(title)  # Join the title using a space separator
        title = title.replace(',', '')  # Remove commas from the concatenated title

        content = response.css('p::text').getall()
        content = ' '.join(content)  # Join the content using a space separator
        item['content'] = content

        content = content.replace(',', '')  # Remove commas from the concatenated content

        # Concatenate title and content into a single field called 'title'
        item['title'] = title + content

        yield item
