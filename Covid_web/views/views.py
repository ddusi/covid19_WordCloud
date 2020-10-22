from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from Covid_web.models import Question, Answer
from Covid_web.forms import AnswerForm


def index(request):
	return render(request, 'Covid_web/index.html')


def QnA(request):
	questions = Question.objects
	return render(request, 'Covid_web/QnA.html', {'object': Question, 'questions': questions})


def ques(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	answers = question.answers.all()
	return render(request, 'Covid_web/Question.html', {'object': Question, 'question': question, 'answers': answers})


def new(request):
	return render(request, 'Covid_web/new.html')


def create(request):
	if (request.method == 'POST'):
		post = Question()
		post.question_text = request.POST['question_text']
		post.save()
	return redirect('covid:QnA')


def answer(request, question_id):
	if (request.method == "POST"):
		answer_form = AnswerForm(request.POST)
		answer_form.instance.question_id = question_id
		if answer_form.is_valid():
			answer = answer_form.save()
	return HttpResponseRedirect(reverse_lazy('covid:ques', args=[question_id]))


def News(request):
	global article
	context = article
	return render(request, 'Covid_web/News.html', context)


def Precautions(request):
	global pre, Korea, World
	context = {
		"pre": pre,
		'Korea': Korea,
		'World': World,
	}
	return render(request, 'Covid_web/Precautions.html', context)


def basic_information(request):
	global cont
	context = {
		'cont': cont[1:-21]
	}
	return render(request, 'Covid_web/basic_information.html', context)
