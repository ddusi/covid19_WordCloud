from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from os.path import dirname, abspath, join
import sqlite3
from datetime import date
import time

root_path = dirname(dirname(dirname(abspath(__file__))))


def return_data_frame(table: str) -> 'DataFrame':
	conn = sqlite3.connect(join(root_path, 'db.sqlite3'))
	sql = 'SELECT * FROM ' + table + ' WHERE created_at LIKE ' + '\'' + str(date.today()) + '%\''
	df = pd.read_sql(sql, index_col='index', con=conn)
	conn.close()
	return df


def save_data_frame(df: 'DataFrame', table: str) -> 'Success Message':
	conn = sqlite3.connect(join(root_path, 'db.sqlite3'))
	c = conn.cursor()
	sql = 'SELECT COUNT(created_at) FROM ' + table + ' WHERE created_at LIKE ' + '\'' + str(date.today()) + '%\''
	# sql = 'SELECT COUNT(created_at) FROM ' + table + ' WHERE created_at LIKE ' + '\'' + '2020-11-0' + '%\''
	try:
		data = c.execute(sql).fetchall()
	except:
		return print('-------------------------------- Not exist ' + table + ' --------------------------------')

	if data[0][0] == 0:
		df.to_sql(name=table, con=conn, if_exists='append', index=False, index_label='index')
		conn.close()
		return print('-------------------------------- ' + str(
			date.today()) + ' success save ' + table + ' --------------------------------')
	else:
		conn.close()
		return print('-------------------------------- ' + str(
			date.today()) + ' Already existing data ' + table + ' --------------------------------')


def get_original_url(table: str, df: 'DataFrame'):
	origin_url_list: list = []
	origin_url_dict: dict = {}
	# df: 'DataFrame' = return_data_frame(table)
	url_list: list = list(df['url'])

	driver = webdriver.Chrome(join(root_path, 'chromedriver.exe'))
	count = 0
	for i in url_list:
		driver.get(i)
		time.sleep(2)
		try:`
			contents_url: str = driver.current_url
			origin_url_list.append(contents_url)
		except common.exceptions.NoSuchElementException:
			origin_url_list.append('')
			pass
		count += 1
		print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ' + count + ' / ' + len(df) + ' <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

	# sql update
	origin_url_dict['origin_url'] = origin_url_list
	# df = df.head(n=3)
	origin_url_dict['index'] = [i for i in range(len(df))]
	df_ = pd.DataFrame(origin_url_dict)
	new_df = pd.merge(df, df_, how='outer', on='index')

	save_data_frame(new_df, table)



# company filtering 함수로 보내기
# filter_company(df)

# def filter_company(b):
# 	# company에 있는 뉴스사들만 추출하기
# 	company_list = ['newsBTC', 'Cointelegraph', 'CoinTelegraph', 'Coindesk', 'BelnCrypto', 'Bitcoinist', 'Bitcoin News',
# 	                'CNBC', 'The Guardian', 'BBC news', 'Reuters', 'Business Week', 'The Economist',
# 	                'Bloomberg', 'The Wall Street Journal', 'Forbes', 'Bitcoin News (press release)', 'CoinDesk']
# 	filter_df = b[b['company'].isin(company_list)]
#
# 	return filter_df

if __name__ == "__main__":
	df = {'index':[0,1,2], 'url':['https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html','https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html','https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html']}
	df = pd.DataFrame(df)
	get_original_url('covid19_article', df)
