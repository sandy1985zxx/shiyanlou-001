# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    @property
    def start_urls(self):
        tmpl_url='https://github.com/shiyanlou?page={}&tab=repositories'
        return (tmpl_url.format(i) for i in range(1,5))

     

    def parse(self, response):
        for course in response.css('li.col-12'):
            item = ShiyanlouItem({
                'name':course.xpath(".//h3/a/text()").extract_first().strip(),
                'update_time':course.xpath('.//relative-time/@datetime').extract_first()
                 
                })
            yield item

        
