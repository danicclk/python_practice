import scrapy
from scrapy_splash import SplashRequest


class QuotesJSSpider(scrapy.Spider):
    name = 'quotejs'

    start_urls = ['https://www.indeed.com/q-developer-l-Evanston,-IL-jobs.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        # follow links to job description page
        for href in response.css('.clickcard .jobtitle::attr(href)'):
            yield response.follow(href, self.parse_jobs)

        # follow pagination links
        for href in response.css('.pagination a:last-child::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_jobs(self, response):
        def extract_with_css(query):
            if response.css(query).extract_first():
                return response.css(query).extract_first().strip()
            else:
                return ''

        yield {
            # 'job_title': extract_with_css('.jobtitle::text'),
            # 'company': extract_with_css('.company::text'),
            # 'snip': extract_with_css('.snip::text'),
            'page_title': extract_with_css('title::text')
        }
