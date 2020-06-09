# -*- coding: utf-8 -*-
import scrapy
import json
import csv
from csv import reader,writer

class ChangeuserSpider(scrapy.Spider):
    name = 'changeuser'

    companynameread = open('lefturl.csv','r')
    readdata = reader(companynameread)
    start_urls = [url[0] for url in readdata]

    def parse(self, response):
        body = response.body
        try:
            data = json.loads(body.decode())
            yield data
        
        except Exception as e:
            print(e)
    