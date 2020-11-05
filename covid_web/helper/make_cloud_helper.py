import os
import pandas as pd
import re
import nltk
from nltk import FreqDist

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator


def make_data():
	'''
	- crawing_data for covide19
	- make word cloud
	'''
	os.system('scrapy runspider covid_web/scrapy/covid/spiders/covid_spider.py')
	make_cloud_helper('covid_WordCloud.png')


def make_cloud_helper(name: 'file name.png'):
	'''
	Create WordCloud picture .png
	'''
	article_pd = pd.read_csv('article.csv')

	# NLTK string preprocessing
	headlines = list(article_pd['headline'])
	headlines = '.'.join(headlines)
	letters_only = re.sub('[^a-zA-Z]', ' ', headlines)
	lower_case = letters_only.lower()
	words = lower_case.split()
	tagged = nltk.pos_tag(words)

	stop_words = ['daily', 'roundup', 'update', 'july', 'sunday', 'aug', 'list', 'line']
	name_list = [t[0] for t in tagged if t[1] != "VB" and t[0] not in stop_words and t[1] == "NN"]
	fd_names = FreqDist(name_list)

	# image dataization
	covid_color = np.array(Image.open(os.path.join("covid_web/static", "covid_person_new.jpg")))
	covid_mask = covid_color.copy()
	covid_mask[covid_mask.sum(axis=2) == 0] = 255

	edges = np.mean([gaussian_gradient_magnitude(covid_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
	covid_mask[edges > .08] = 255

	wc = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA", max_words=2000, mask=covid_mask,
	               max_font_size=40, random_state=42, relative_scaling=0)

	# wc = WordCloud(background_color="black", max_words=2000, mask=covid_mask,
	#                max_font_size=40, random_state=42, relative_scaling=0)

	wc.generate_from_frequencies(fd_names)
	# wc.generate(text)
	image_colors = ImageColorGenerator(covid_color)
	wc.recolor(color_func=image_colors)
	wc.to_file("covid_web/static/" + name)
