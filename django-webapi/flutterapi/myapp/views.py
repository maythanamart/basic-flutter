from urllib import response
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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

