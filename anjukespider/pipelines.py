# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 获取的数据比较杂乱，使用正则清洗数据
import csv
import re
def list2str(value):
    new = ''.join(value).strip()
    return new

class AnjukespiderPipeline(object):
    def __init__(self):
        a = open('item.csv', 'a', newline='',encoding="utf-8")
        self.writer = csv.writer(a, csv.QUOTE_ALL)

    def process_item(self, item, spider):

        area = item['area']
        price = item['price']
        loc = item['location']
        district = item['district']
        mode = item['mode']
        age = item['age']
        floor = item['floor']

        modes = list2str(mode)
        item['area'] = re.findall(r'\d+', list2str(area))[0]
        item['age'] = re.findall(r'\d+', list2str(age))[0]
        item['floor'] = list2str(floor)
        item['location'] = list2str(loc)
        item['district'] = list2str(district)
        item['price'] = re.findall(r'\d+', list2str(price))[0]
        item['mode'] = modes.replace('\t', '').replace('\n', '')

        self.writer.writerow([item['area'], item['age'], item['floor'], item['location'], item['district'], item['price'], item['mode']])

        return item

    def close_spider(self, spider):
        self.writer.close()


