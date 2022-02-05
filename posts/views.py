
from attr import validate
from django.shortcuts import render
from .serializer import PostSerializerImageField
from rest_framework import viewsets
from .models import Posts
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from posts import serializer
from rest_framework import status

class PostView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializerImageField
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        
        data['user_id'] = request.user.id
        print(data)
        serializer = PostSerializerImageField(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

        

# class PostView(ListAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializerAllField
#     permission_classes = [IsAuthenticated]


        
