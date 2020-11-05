import scrapy
import pandas as pd
from datetime import date
import sqlite3
from os.path import dirname, abspath, join
import sys
root_path = dirname(dirname(dirname(dirname(dirname(abspath(__file__))))))
sys.path.append(join(root_path, 'covid_web', 'helper'))
from get_original_url_helper import get_original_url



class CovidSpider(scrapy.Spider):
	name = "covid_article"
	start_urls = [
		'https://news.google.com/search?q=covid19&hl=en-US&gl=US&ceid=US%3Aen',
	]

	def parse(self, response):
			dic = {'headline': [], 'company': [], 'time': [], 'url': []}
			headline = response.css('.DY5T1d::text').getall()
			company = response.css('.wEwyrc::text').getall()
			time = response.css('.WW6dff::text').getall()
			urls = response.css('.DY5T1d::attr(href)').getall()
			dic['headline'] = headline
			dic['company'] = company
			dic['time'] = time
			dic['url'] = ['https://news.google.com%s' % url.split('.')[1] for url in urls]
			dic['index'] = [i for i in range(len(urls))]
			# dic.drop(columns='Unnamed: 0',inplace=True)

			# pd.DataFrame(dic).to_csv('article.csv')

			df = pd.DataFrame(dic)
			df['created_at'] = pd.to_datetime(str(date.today()), format='%Y-%m-%d')
			# save_data_frame(df, 'covid19_article')
			get_original_url('covid19_article', df)
