# -*- coding: utf-8 -*-
import scrapy, csv
from scrapy import Request
import requests, json, re
from collections import OrderedDict
from scrapy.http import TextResponse
from json import loads

from get_data_from_directories.spiders.base.base_spider import BaseSpider


class One1888_gr_spider(BaseSpider):

	name = "One1888_gr"

	start_urls = [
		'https://www.11888.gr/yellow-pages/%CE%93%CE%B5%CF%89%CF%81%CE%B3%CE%B9%CE%BA%CE%AC-%CE%95%CE%AF%CE%B4%CE%B7-%CE%BA%CE%B1%CE%B9-%CE%A0%CF%81%CE%BF%CF%8A%CF%8C%CE%BD%CF%84%CE%B1/?location=%CE%A7%CE%B1%CE%BD%CE%B9%CE%AC&amp;lat=35.5138298&amp;lng=24.01803670000004'
	]

	use_selenium = True
###########################################################

	def __init__(self, *args, **kwargs):
		super(BaseSpider, self).__init__(*args, **kwargs)


###########################################################
	def start_requests(self):
		for url in self.start_urls:
			yield Request(url=url, callback=self.parseItems, dont_filter=True, meta={'url':url, 'page_num': 1})

	def parseItems(self, response):
		try:
			script_data = response.xpath('//script[@type="application/ld+json"]/text()').extract_first()
			json_data = loads(script_data)

			if json_data.get('itemListElement'):
				for item in json_data.get('itemListElement'):
					url = item.get('url')
					if url:
						yield scrapy.Request(url, callback=self.parseItem, dont_filter=True)
		except:
			return

	def parseItem(self, response):
		item = OrderedDict()
		for h in self.data_headers:
			item[h] = ''

		page_desc = response.xpath('//div[@id="list-page-description"]/div[2]')

		name = response.xpath('//div[@id="list-page-description"]/h1/text()').extract_first()
		if name:
			name = name.strip()
		item['name'] = name

		company = page_desc.xpath('./p/text()').extract_first()
		if company:
			company = company.strip()
		item['company'] = company

		region = page_desc.xpath('./p[@class="p-region"]/text()').extract_first()
		if region:
			region = region.strip()
		item['address'] = region

		tel = page_desc.xpath('./p[@class="p-tel"]/text()').extract_first()
		if region:
			tel = tel.strip()
		item['phone'] = tel

		item['detail url'] = response.url

		self.total_count += 1
		print('total_count: ' + str(self.total_count))
		print(item)
		self.result_data_list[str(self.total_count)] = item









