# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import xlsxwriter
import os, pyodbc
from collections import OrderedDict

class get_data_from_directoriesPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


    def spider_opened(self, spider):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Work_Scraping\Greece_Panteleimon_freelancer\get_data_from_directories\output\output.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from table Office_Address_List')

        for row in cursor.fetchall():
            print (row)

    def spider_closed(self, spider):
        pass

    def process_item(self, item, spider):

        return item
