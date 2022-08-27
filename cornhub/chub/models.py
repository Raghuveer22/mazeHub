from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Question(models.Model):
      id=models.AutoField
      title=models.CharField(max_length=100)
      correct_id=models.IntegerField(default=-1)
      wrong_id_1=models.IntegerField(default=-1)
      wrong_id_2=models.IntegerField(default=-1)
      wrong_id_3=models.IntegerField(default=-1)   
      score=models.IntegerField(default=0)
class User_Flow(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
      time = models.DateTimeField(default=datetime.utcnow())
      
      question=models.ForeignKey(Question,on_delete=models.CASCADE,default=1)