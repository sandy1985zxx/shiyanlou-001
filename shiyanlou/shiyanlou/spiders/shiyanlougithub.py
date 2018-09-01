# -*- coding: utf-8 -*-
import scrapy


class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    @property
    def start_usrls(self):
        tmpl_url='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

     

    def parse(self, response):
        for course in response.css('div.course-body')
            item = RepositoriesItem({
                'id':response.css()
                'name':response.css()
                'update_time':response.css()
                })
            yield item

        
