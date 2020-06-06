# -*- coding: utf-8 -*-
import scrapy


class ChangeuserSpider(scrapy.Spider):
    name = 'changeuser'
    start_urls = ['https://www.whatsmyua.info/api/v1/ua?']

    def parse(self, response):
        print(response.body)
