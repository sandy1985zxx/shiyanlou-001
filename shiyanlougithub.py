#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import scrapy


class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlouspider'
    @property
    def start_urls(self):
        url_tmpl = 'http://github.com/shiyanlou?page={}&tab=repositories'


        return (url_tmpl.format(i) for i in range(1,5))
    def parse(self,response):
        for content in response.css('li.col-12'):
            yield {'name':response.xpath(".//h3/a/text()").extract_first().strip(),
            i    'update_time':response.xpath('.//relative-time/@datetime').extract_first()
                }

