from django import forms

from .models import Answer, Question


class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['answer_text']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['answer_text'].label = "answer"


class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question_text', 'password']

	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.fields['answer_text'].label = "answer"
