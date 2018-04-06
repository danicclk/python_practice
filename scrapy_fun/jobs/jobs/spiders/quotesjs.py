import scrapy
from scrapy.splash import SplashRequest


class QuotesSpider(scrapy.Spider):  # define a class
    name = "quotesjs"  # define the variable, identifies the Spider. Must be unique.
      
    def start_requests(self):
        yield SplashRequest(
            url = "http://quotes.toscrape.com/js"
            callback=self.parse,
        )

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield = {
                'text': response.css('span.text::text').extract_first(),
                'author_name': response.css('small.author::text').extract_first(),
                'tag': response.css('a.tag::text').extract(),
            }
        # yield item 
        # follow pagination link
            # this line just gets the relative url
        # next_page_url = response.css('li.next > a::attr(href)').extract_first()
        # if next_page_url: # spider will stop once there're no more pages
           # next_page_url = response.urljoin(next_page_url)
            #the spiderneeds to generate new request
            #yield scrapy.Request(url=next_page_url, callback=self.parse)