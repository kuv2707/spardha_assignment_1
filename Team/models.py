from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=30)
    college=models.TextField(default="faltu sa koi")
