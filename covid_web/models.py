import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.TextField()
    password = models.TextField(default='0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    answer_text = models.CharField(max_length=200)

    class Meta:
        ordering=['id']


class WorldConfirmation(models.Model):
    index = models.IntegerField(null=True)
    Area = models.TextField(null=True)
    Total = models.TextField(null=True)
    Cases = models.TextField(null=True)
    Recovered = models.TextField(null=True)
    Deaths = models.TextField(null=True)
    Trends = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'world_confirmation'


class Covid19Article(models.Model):
    index = models.IntegerField(null=True)
    headline = models.TextField(null=True)
    company = models.TextField(null=True)
    url = models.TextField(null=True)
    time = models.TextField(null=True)
    origin_url = models.TextField(null=True)
    created_at = models.TextField(null=True)

    class Meta:
        db_table = 'covid19_article'

