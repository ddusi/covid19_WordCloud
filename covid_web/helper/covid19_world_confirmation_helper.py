from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl
import pandas as pd
from covid_web.helper.save_dataframe_helper import save_data_frame
from datetime import date


def remove_comma(x: str) -> str:
	return x.replace(',', '')


def covid_confirmation():
	'''
	 make dataFrame to covid19 confirmation and save_data_frame() Call
	'''
	World = {
		'Area': [],
		'Total': [],
		'Cases': [],
		'Recovered': [],
		'Deaths': [],
		'Trends': [],
	}

	# world
	context = ssl._create_unverified_context()
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
	World_URL = 'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'
	req = Request(url=World_URL, headers=headers)

	html = urlopen(req, context=context)

	World_bs = BeautifulSoup(html, 'html.parser')

	World_Num = [n.text.strip() for n in World_bs.find('tbody', {'class': 'ppcUXd'}).findAll('td', {'class': 'l3HOY'})
	             if n.text != ''][:64]
	World_Area = [a.text.strip() for a in
	              World_bs.find('tbody', {'class': 'ppcUXd'}, ).findAll('th', {'class': 'l3HOY'}) if a.text != ''][:16]
	World_Trends = ['https:' + i['src'] for i in
	                World_bs.find('tbody', {'class': 'ppcUXd'}).find_all('img', {'class': 'nBjBX'})][:16]

	World['Area'] = World_Area
	World['Trends'] = World_Trends
	for n in range(len(World_Num)):
		if n % 4 == 0:
			World['Total'].append(World_Num[n])
		elif n % 2 == 0:
			World['Recovered'].append(World_Num[n])
		elif (n - 1) % 4 == 0:
			World['Cases'].append(World_Num[n])
		else:
			World['Deaths'].append(World_Num[n])

	df = pd.DataFrame(World)

	df['created_at'] = pd.to_datetime(str(date.today()), format='%Y-%m-%d')

	save_data_frame(df, 'world_confirmation')

# def get_world_trends_data():
# 	context = ssl._create_unverified_context()
# 	headers = {
# 		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
# 	URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
# 	req = Request(url=URL, headers=headers)
#
# 	html = urlopen(req, context=context)
# 	soup = BeautifulSoup(html, 'html.parser')
