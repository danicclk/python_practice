import scrapy



class QuotesSpider(scrapy.Spider):  # define a class
    name = "quotes"  # define the variable, identifies the Spider. Must be unique.
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]
  
   # call back method
    def parse(self, response):
        self.log('I just visited:' + response.url)
        for quote in response.css('div.quote'):
            items= {
            'author_name': response.css('small.author::text').extract_first(),
            'text': response.css('span.text::text').extract_first(),
            'tage': response.css('a.tag::text').extract(),
            }
            yield item 
        # follow pagination link
        