# -*- coding: utf-8 -*-
import scrapy


class ChangeuserSpider(scrapy.Spider):
    name = 'changeuser'
    start_urls = ['https://www.crunchbase.com/v4/data/entities/organizations/-2p--twopix-technologies?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,%22title%22,%22short_description%22,%22is_locked%22%5D&layout_mode=json']

    def parse(self, response):
        print(response.body)
