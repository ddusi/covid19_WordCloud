from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from ..helper.get_info import Covid_confirmed
# from ..helper.covid19_basic_and_precaution_info_crawl_helper import basic, precaution
from ..helper.make_cloud_helper import make_cloud_helper
from multiprocessing import Process, current_process
import pandas as pd
import os

flag = True
article = {}
cont = []
pre = []
Korea = {}
World = {}


def make_data():
	os.system('scrapy runspider covid_web/scrapy/covid/spiders/covid_spider.py')
	global Korea, World
	make_cloud_helper('covid_WordCloud.png')
	Korea, World = Covid_confirmed()


def home(request):
	return render(request, 'covid_web/home.html')


def news(request):
	article_pd = pd.read_csv('article.csv')
	article = article_pd.to_dict()
	print(article)
	return render(request, 'covid_web/news.html', article)


def covid_info(request):
	global cont
	context = {
		'cont': cont[1:-21]
	}
	return render(request, 'covid_web/covid_info.html', context)


def status(request):
	return render(request, 'covid_web/status.html')
