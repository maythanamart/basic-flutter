from lib2to3.pgen2 import token
from pickle import TRUE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100,default='member')
    mobile = models.CharField(max_length=100, null=True, blank=True)
    token = models.CharField(max_length=100, default='-')
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username