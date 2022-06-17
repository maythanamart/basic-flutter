from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home),
    path('api/all-todolist/',all_todolist),
    path('api/add-todolist', add_todolist),
    path('api/update-todolist/<int:TID>', update_todolist),
    path('api/delete-todolist/<int:TID>', delete_todolist),
    path('api/newuser', register_newuser),
    path('api/auth', authenticate_app)
]