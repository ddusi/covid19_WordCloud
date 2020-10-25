from django.views.generic import View
from ..forms import QuestionForm
from Covid_web.models import Question
from django.shortcuts import render, redirect


class QuestionCRUDView(View):
	http_method_names = ['get', 'post', 'put', 'delete']

	def __init__(self):
		self.questions = Question.objects
		self.form = QuestionForm()

	def dispatch(self, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()
		if method == 'put':
			return self.put(*args, **kwargs)
		if method == 'delete':
			return self.delete(*args, **kwargs)
		return super(QuestionCRUDView, self).dispatch(*args, **kwargs)

	def get(self, *args, **kwargs):
		return render(self.request, 'covid_web/precautions.html', {'form': self.form, 'questions': self.questions})

	def post(self, *args, **kwargs):
		form = QuestionForm(self.request.POST)
		if form.is_valid():
			form.save()
		return redirect('/covid-web/precautions', {'form': form, 'questions': self.questions})

	def delete(self, *args, **kwargs):
		data = Question.objects.get(pk=self.request.POST['pk'])
		if data.password == self.request.POST['password']:
			data.delete()
			return render(self.request, 'covid_web/precautions.html', {'form': self.form, 'questions': self.questions})
		else:
			return redirect('/covid-web/precautions', {'form': self.form, 'questions': self.questions, 'error':'password not match'})
