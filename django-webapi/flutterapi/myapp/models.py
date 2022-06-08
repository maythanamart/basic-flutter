from turtle import title
from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title