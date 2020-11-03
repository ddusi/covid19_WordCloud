import scrapy
import pandas as pd
import sqlite3
from datetime import date
from os.path import dirname, abspath, join

root_path = dirname(dirname(dirname(dirname(dirname(abspath(__file__))))))

def save_data_frame(df, table):
	conn = sqlite3.connect(join(root_path, 'db.sqlite3'))
	c = conn.cursor()
	sql = 'SELECT COUNT(created_at) FROM ' + table + ' WHERE created_at LIKE ' + '\'' + str(date.today()) + '%\''
	# sql = 'SELECT COUNT(created_at) FROM ' + table + ' WHERE created_at LIKE ' + '\'' + '2020-11-0' + '%\''
	data = c.execute(sql).fetchall()

	if data[0][0] == 0:
		df.to_sql(name=table, con=conn, if_exists='append', index=True)
		conn.close()
		return print('-------------------------------- ' + str(
			date.today()) + ' success save ' + table + ' --------------------------------')
	else:
		conn.close()
		return print('-------------------------------- ' + str(
			date.today()) + ' Already existing data ' + table + ' --------------------------------')


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

		# dic.drop(columns='Unnamed: 0',inplace=True)

		# pd.DataFrame(dic).to_csv('article.csv')

		df = pd.DataFrame(dic)
		df['created_at'] = pd.to_datetime(str(date.today()), format='%Y-%m-%d')
		save_data_frame(df, 'covid19_article')
