from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class Place(models.Model):
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True, null=True) 
