# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from aqlalchemy.orm import sessionmaker
from shiyanlou.models import Respository,engine
from datetime import datetime
class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['id']=int(item['id']
        item['name']=string(item['name'])
        item['update_time']=datetime.strptime(item['update_time'])[0],'%Y-%m-%d']
        self.session.add(Repository(**item))
        return item
    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()


