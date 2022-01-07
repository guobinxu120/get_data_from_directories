# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.conf import settings
from scrapy.linkextractors import LinkExtractor

import re



class BaseSpider(CrawlSpider):
	""" Spider for site :
	"""
	name = "base_spider"

	products_count = 0
	max_products_count = 100

	total_count = 0
	result_data_list = {}
	filepath = ''
	data_headers = ['name', 'company', 'email', 'mobile', 'phone', 'website', 'detail url', 'address', 'city', 'prefecture']

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		# 'Accept-Language': 'en-US,en;q=0.5',
		# 'Accept-Encoding': 'gzip, deflate',
		# 'Connection': 'keep-alive'
	}

	headers_ajax = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type':'application/json; charset=UTF-8',
		'X-Requested-With':'XMLHttpRequest'
	}

	def __init__(self):
		settings.set('RETRY_HTTP_CODES', [503, 504, 400, 408, 404] )
		settings.set('RETRY_TIMES', 5)
		settings.set('REDIRECT_ENABLED', True)
		settings.set('METAREFRESH_ENABLED', True)


	def removeSpace(self, text):
		""" Function for remove space of text
		"""
		return re.sub(r'(\s+)', ' ', text).strip()

	def removeTags(self, text):
		""" exec regex pattern on text and remove matching string at group
		"""
		return re.sub(r'(<.*?>)', '', text).strip()


	def getText(self, selector, xpath):
		""" Exec xpath query on selector and return first match as string
		"""
		vals = selector.xpath(xpath).extract()
		if len(vals) > 0:
			return vals[0].strip()
		else:
			return ''


	def getTexts(self, selector, xpath, dont_filter=True):
		""" Exec xpath query on selector and return all match as list of string
		"""
		return [x.strip() for x in selector.xpath(xpath).extract() if dont_filter or x.strip() != '' ]


	def getTextAll(self, selector, xpath, join_string=' '):
		""" Exec xpath query on selector and return all match as string
		"""
		return join_string.join( [x.strip() for x in selector.xpath(xpath).extract()] ).strip()


	def reText(self, text, pattern, group=1):
		""" exec regex pattern on text and return matching string at group
		"""
		match = re.search( pattern, text)
		if match != None:
			return match.group(group)
		else:
			return ''
