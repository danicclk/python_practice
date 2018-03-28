import scrapy



class QuotesSpider(scrapy.Spider):  # define a class
    name = "quotes"  # define the variable, identifies the Spider. Must be unique.
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]
  
   # call back method
    def parse(self, response):
        self.log('I just visited:' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'author_name': response.css('small.author::text').extract_first(),
                'text': response.css('span.text::text').extract_first(),
                'tage': response.css('a.tag::text').extract(),
            }
            yield item 
        # follow pagination link
            # this line just gets the relative url
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url: # spider will stop once there're no more pages
            next_page_url = response.urljoin(next_page_url)
            # the spiderneeds to generate new request
            yield scrapy.Request(url=next_page_url, callback=self.parse)