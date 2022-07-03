from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    userid = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    day = models.CharField(max_length=100)
    reminder = models.BooleanField()
