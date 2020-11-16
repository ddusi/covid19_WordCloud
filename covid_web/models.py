import datetime

from django.db import models
from django.utils import timezone
from datetime import date


class Question(models.Model):
	question_text: str = models.TextField()
	password: str = models.TextField(default='0000')
	created_at: date = models.DateTimeField(auto_now_add=True)
	updated_at: date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question_text


class Answer(models.Model):
	question: Question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
	answer_text: str = models.CharField(max_length=200)

	class Meta:
		ordering = ['id']


class WorldConfirmation(models.Model):
	index: int = models.IntegerField(null=True)
	Area: str = models.TextField(null=True)
	Total: str = models.TextField(null=True)
	Cases: str = models.TextField(null=True)
	Recovered: str = models.TextField(null=True)
	Deaths: str = models.TextField(null=True)
	Trends: str = models.TextField(null=True)
	created_at: date = models.DateTimeField(null=True)

	class Meta:
		db_table = 'world_confirmation'


class Covid19Article(models.Model):
	index: int = models.IntegerField(null=True)
	headline: str = models.TextField(null=True)
	company: str = models.TextField(null=True)
	url: str = models.TextField(null=True)
	time: str = models.TextField(null=True)
	origin_url: str = models.TextField(null=True)
	created_at: date = models.TextField(null=True)

	class Meta:
		db_table = 'covid19_article'
