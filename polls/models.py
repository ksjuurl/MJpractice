import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)    # 질문내용
    pub_date = models.DateField('date published')       # 질문생성날짜

    #모든내용표시하기
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #  선택지에해당하는 질문
    choice_text = models.CharField(max_length=200)  # 상세내용    
    votes = models.IntegerField(default=0)          # 투표수

    #모든내용표시하기
    def __str__(self):
        return self.choice_text


