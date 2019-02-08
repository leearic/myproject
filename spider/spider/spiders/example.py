# -*- coding: utf-8 -*-
import scrapy








class ExampleSpider(scrapy.Spider):
    name = 'e'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):


        self.logger.error(response.text)

        


        pass


