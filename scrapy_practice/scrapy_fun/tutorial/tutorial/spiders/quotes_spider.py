import scrapy
from scrapy_splash import SplashRequest


class QuotesJSSpider(scrapy.Spider):
    name = 'quotejs'

    def start_requests(self):
        yield SplashRequest(
            url='',
            callback=self.parse,
        )

    def parse(self, response):
        for quote in response.css("div.quote"):
            # css selectors below
            yield {
            }

        # follow links to job description page


        # yield {
        #     # 'job_title': extract_with_css('.jobtitle::text'),
        #     # 'company': extract_with_css('.company::text'),
        #     # 'snip': extract_with_css('.snip::text'),
        #     'page_title': extract_with_css('title::text')
        # }
