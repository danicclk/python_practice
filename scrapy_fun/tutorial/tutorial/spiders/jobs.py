import scrapy



class JobsSpider(scrapy.Spider):  # define a class
    name = "jobs"  # define the variable, identifies the Spider. Must be unique.
    #allowed_domains = ["toscrape.com"]
    start_urls = ["https://www.indeed.com/jobs?q=junior%20software%20developer&l=Chicago%2C%20IL"]
  
   # call back method
    def parse(self, response):
        urls = response.css('div.quote > span > a::attr(href)').extract() #CHANGE
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
        # follow pagination link
            # this line just gets the relative url
        #next_page_url = response.css('li.next > a::attr(href)').extract_first()
        next_page_url = response.css('div.pagination > a::attr(href)').extract_first()
        if next_page_url: # spider will stop once there're no more pages
            next_page_url = response.urljoin(next_page_url)
            # the spiderneeds to generate new request
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        yield {
            'job_title': response.css('b.jobtitle::text').extract_first(),
            #'company': response.css('span.company::text').extract_first()
        }