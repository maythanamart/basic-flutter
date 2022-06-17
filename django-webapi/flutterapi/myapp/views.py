from urllib import response
import django
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import uuid

@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'created'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_todolist(request, TID):
    if request.method == 'PUT':
        data = {}
        todo = Todolist.objects.get(id=TID)
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_todolist(request, TID):
    if request.method == 'DELETE':
        data = {}
        todo = Todolist.objects.get(id=TID)
        delete = todo.delete()
        #serializer = TodolistSerializer(todo, data=request.data)
        if delete:
            data['status'] = 'deleted'
            return Response(data=data, status=status.HTTP_200_OK)
        data['status'] = 'failed'
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def register_newuser(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        usertype = data.get('usertype')
        mobile = data.get('mobile')
        
        if username == None and password == None:
            print('username & password required')
            return Response(data={'status':'username and password required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            User.objects.get(username=username)
            print('user-exist')
            return Response(data={'status': 'user-exist'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            newuser = User()
            newuser.username = username
            newuser.set_password(password)
            newuser.first_name = first_name
            newuser.last_name = last_name
            newuser.save()
            
            newprofile = Profile()
            user = User.objects.get(username=username)
            newprofile.user = user
            newprofile.usertype = '' if usertype == None else usertype
            newprofile.mobile = mobile
            gentoken = uuid.uuid1().hex
            newprofile.token = gentoken
            newprofile.save()
            print('user-created')
            return Response(data={'status': 'user-created', 
                                'token': gentoken,
                                'first_name': first_name,
                                'last_name': last_name,
                                'username': username }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authenticate_app(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        
        try:
            user = authenticate(username=username, password=password)
            login(request, user)
            user = User.objects.get(username=username)
            return Response(data={'status': 'success', 
                                'token': user.profile.token,
                                'first_name': user.first_name,
                                'last_name': user.last_name,
                                'username': username }, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(data={'status': 'failed'}, status=status.HTTP_404_NOT_FOUND)


data = [
    {
        "title":"189/26",
        "subtitle":"เม็ดมะม่วงหิมพานต์ Size King เกรด AAA",
        "image_url":"https://raw.githubusercontent.com/maythanamart/basic-api/main/beans.jpg",
        "detail":"รายละเอียด1..."
    },
    {
        "title":"189/27",
        "subtitle":"ทุเรียนหมอนทอง กรอบ อร่อย",
        "image_url":"https://raw.githubusercontent.com/maythanamart/basic-api/main/durian.jpg",
        "detail":"รายละเอียด2..."
    },
    {
        "title":"189/28",
        "subtitle":"อาหารญี่ปุ่น ทำสดใหม่ทุกวัน",
        "image_url":"https://raw.githubusercontent.com/maythanamart/basic-api/main/salmon.jpg",
        "detail":"รายละเอียด3..."
    },
    {
        "title":"189/29",
        "subtitle":"เสื้อผ้าน้องหมา น่ารัก สุดคิ้ว",
        "image_url":"https://raw.githubusercontent.com/maythanamart/basic-api/main/dog_clothes.jpg",
        "detail":"รายละเอียด4..."
    }
]

def Home(request):
    return JsonResponse(data=data, safe=False,json_dumps_params={'ensure_ascii':False})

