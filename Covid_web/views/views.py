from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from Covid_web.models import Question, Answer
from Covid_web.forms import AnswerForm
from ..helper.get_info import basic, precaution, Covid_confirmed, Make_Cloud
from ..helper.make_cloud_helper import make_cloud_helper
import threading
import pandas as pd

flag = True
article = {}
cont = []
pre = []
Korea = {}
World = {}


def make():
	global flag, cont, article, pre, Korea, World
	timer = threading.Timer(600, make)

	if flag:
		make_cloud_helper('covid_WordCloud.png')
		flag = False
	else:
		make_cloud_helper('covid_WordCloud1.png')
		flag = True
	article_pd = pd.read_csv('article.csv')
	article = article_pd.to_dict()
	cont = basic()
	pre = precaution()
	Korea, World = Covid_confirmed()
	timer.start()


make()


def home(request):
	return render(request, 'covid_web/home.html')


def news(request):
	global article
	context = article
	return render(request, 'covid_web/news.html', context)


def covid_info(request):
	global cont
	context = {
		'cont': cont[1:-21]
	}
	return render(request, 'covid_web/covid_info.html', context)


def precautions(request):
	global pre, Korea, World
	context = {
		"pre": pre,
		'Korea': Korea,
		'World': World,
	}
	return render(request, 'covid_web/precautions__.html', context)


def status(request):
	return render(request, 'covid_web/status.html')
