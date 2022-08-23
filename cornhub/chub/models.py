from django.db import models
from django.contrib.auth.models import User

class score(models.Model):
    player=models.ForeignKey(User,on_delete=models.CASCADE)
    points=models.IntegerField(default=0)
    # time_taken=


