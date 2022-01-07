# -*- coding: utf-8 -*-
#!/usr/bin/python
from multiprocessing import Pool
import os, sys, csv, platform, datetime, glob


def _crawl(spider_name_params=None):
	if spider_name_params:
		print spider_name_params
		# print ">>>>> Starting {} spider".format(spider_name_params)
		command = 'scrapy crawl {} -o {}.csv'.format(spider_name_params, spider_name_params)

		os.system(command)
		# print "finished."
	return None

def run_crawler(spider_names):

	for spider_name in spider_names:

		pool = Pool(processes=5)
		pool.map(_crawl, [spider_name])

if __name__ == '__main__':
	spider_names = []
	if len(sys.argv) == 1:
		spider_names = ['fruugo_co_uk_Clothing', 'fruugo_co_uk_Electricals', 'fruugo_co_uk_Food_Drink',
						'fruugo_co_uk_Health_Beauty', 'fruugo_co_uk_Home_Garden', 'fruugo_co_uk_Kids_Toys',
						'fruugo_co_uk_Sports_Leisure']
	elif len(sys.argv) == 2:
		spider_names = [sys.argv[1]]
	run_crawler(spider_names)
