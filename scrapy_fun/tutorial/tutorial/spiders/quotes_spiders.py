import scrapy


class QuotesSpider(scrapy.Spider):  # define a class
	name = "quotes"  # define the variable, identifies the Spider. Must be unique.

	def start_requests(self): # start a function
		urls = [
			'http://quotes.toscrape.com/page/1/',  # extract the html of these pages
			'http://quotes.toscrape.com/page/2/'
		]
		for url in urls: # loop to those urls
			yield scrapy.Request(url=url, callback=self.parse) # implement the callback function

	def parse(self, response):
		# checking url, splitting it by characters, extracting the last 2 characters, store in page variable
		page = response.url.split("/")[-2]  
		filename = 'quotes-%s.html' % page  # use that page name and place the string % 
		with open(filename, 'wb') as f:
			f.write(response.body)  # extracting the body
		self.log('Saved file %s' % filename)  # passing string in to file name, spit out in the terminal