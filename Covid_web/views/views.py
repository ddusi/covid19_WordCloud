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
	timer = threading.Timer(30, make)

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
	return render(request, 'Covid_web/home.html')


def news(request):
	global article
	context = article
	return render(request, 'Covid_web/news.html', context)


def covid_info(request):
	global cont
	context = {
		'cont': cont[1:-21]
	}
	return render(request, 'Covid_web/covid_info.html', context)


def qna(request):
	questions = Question.objects
	return render(request, 'Covid_web/qna.html', {'object': Question, 'questions': questions})


def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	answers = question.answers.all()
	return render(request, 'Covid_web/question.html', {'object': Question, 'question': question, 'answers': answers})


def new_question(request):
	return render(request, 'Covid_web/new_question.html')


def create(request):
	if (request.method == 'POST'):
		post = Question()
		post.question_text = request.POST['question_text']
		post.save()
	return redirect('covid:qna')


def answer(request, question_id):
	if (request.method == "POST"):
		answer_form = AnswerForm(request.POST)
		answer_form.instance.question_id = question_id
		if answer_form.is_valid():
			answer = answer_form.save()
	return HttpResponseRedirect(reverse_lazy('covid:question', args=[question_id]))


def precautions(request):
	global pre, Korea, World
	context = {
		"pre": pre,
		'Korea': Korea,
		'World': World,
	}
	return render(request, 'Covid_web/precautions.html', context)
