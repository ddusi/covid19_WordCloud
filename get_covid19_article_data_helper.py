from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl
import os
import sqlite3
from bs4.element import Comment
from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator
import nltk
import spacy
import pandas as pd

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def tag_visible(element):
	if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
		return False
	if isinstance(element, Comment):
		return False
	return True


def text_from_html(html: 'body_data'):
	soup = BeautifulSoup(html, 'html.parser')
	texts = soup.findAll(text=True)
	visible_texts = filter(tag_visible, texts)
	return u" ".join(t.strip() for t in visible_texts)


def get_crawl_body_data(url: str):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; + Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
	req = Request(url=url, headers=headers)
	context = ssl._create_unverified_context()
	html = urlopen(req, context=context).read()

	return html


def make_cloud_helper(name: 'file name.png', article_data: 'article_datas', image_name: 'image.png', recolor: bool):
	'''
	Create WordCloud picture .png
	'''

	# image dataization
	covid_color = np.array(Image.open(os.path.join(BASE_DIR, "covid_web/static", image_name)))
	covid_mask = covid_color.copy()
	covid_mask[covid_mask.sum(axis=2) == 0] = 255

	edges = np.mean([gaussian_gradient_magnitude(covid_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
	covid_mask[edges > .08] = 255

	wc = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA", max_words=1000, mask=covid_mask,
	               max_font_size=110, random_state=42, relative_scaling=0)

	# wc = WordCloud(background_color="black", max_words=2000, mask=covid_mask,
	#                max_font_size=40, random_state=42, relative_scaling=0)

	wc.generate_from_frequencies(article_data)
	# wc.generate(text)
	if recolor:
		image_colors = ImageColorGenerator(covid_color)
		wc.recolor(color_func=image_colors)
	wc.to_file(os.path.join(BASE_DIR, "covid_web/static/" + name))


def return_data_frame(table: str) -> 'DataFrame':
    #conn = sqlite3.connect(settings.DATABASES['default']['NAME'])
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'))
    # sql = 'SELECT * FROM ' + table + ' WHERE created_at LIKE ' + '\'' + str(date.today()) + '%\''
    sql = 'SELECT * FROM ' + table + ' WHERE created_at LIKE ' + '\'' + '2020-11-05' + '%\''
    df = pd.read_sql(sql, index_col='index', con=conn)
    conn.close()
    return df


def main_crawl():
	result = []

	# urls data get from DB
	df = return_data_frame('covid19_article')
	urls = df['origin_url'].values.tolist()

	# get start crawl article body
	cnt = 0
	for url in urls:
		print('------ get start data ' + str(cnt) + '/' + str(len(urls)) + '--------')
		try:
			html = get_crawl_body_data(url)
			data_text = text_from_html(html)
		except:
			pass
		result.append(data_text)
		cnt += 1

	# local place data count
	nlp_wk = spacy.load('xx_ent_wiki_sm')
	doc = nlp_wk(str(result[:50]))
	loc = [ent.text for ent in doc.ents if ent.label_ in ['LOC']]
	doc2 = nlp_wk(str(result[50:]))
	loc2 = [ent.text for ent in doc2.ents if ent.label_ in ['LOC']]
	loc.extend(loc2)

	stop_word = ['COVID-19', 'Gov', 'St', 'States', 'U.S.', 'Wood', 'The', 'A']
	article_data = nltk.FreqDist(loc)
	for word in stop_word:
		try:
			article_data.pop(word)
		except:
			pass
	print(article_data.most_common(100))

	# make word_cloud
	make_cloud_helper(name='place_WordCloud.png', article_data=article_data, image_name='place_pin.png', recolor=False)
main_crawl()