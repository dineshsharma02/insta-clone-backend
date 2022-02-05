
from django.shortcuts import render
from .serializer import PostSerializerImageField
from rest_framework import viewsets
from .models import Posts
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from posts import serializer

class PostView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializerImageField
    permission_classes = [IsAuthenticated]
    
        
        

# class PostView(ListAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializerAllField
#     permission_classes = [IsAuthenticated]


        
