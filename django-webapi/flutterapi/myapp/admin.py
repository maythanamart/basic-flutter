from django.contrib import admin
from .models import Todolist, Profile

# Register your models here.
admin.site.register(Todolist)
admin.site.register(Profile)