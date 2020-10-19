import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    answer_text = models.CharField(max_length=200)

    class Meta:
        ordering=['id']