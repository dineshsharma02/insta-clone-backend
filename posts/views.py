
from os import stat
from attr import validate
from django.http import QueryDict
from django.shortcuts import render
from .serializer import PostSerializerImageField,Postlike_Serializer
from rest_framework import viewsets
from .models import Post_Item,Post_like
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from posts import serializer
from rest_framework.decorators import api_view
from rest_framework import status

class PostView(ListCreateAPIView):
    queryset = Post_Item.objects.all()
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

class PostLike_View(ListCreateAPIView):
    queryset = Post_like.objects.all()
    serializer_class = Postlike_Serializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        user_id = request.user.id
        data = QueryDict(request.data,mutable=True)
        data['user_id'] = request.user.username
        print(data)
        serializer = Postlike_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Post Liked'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


class PostItem_Like(ListAPIView):
    
    serializer_class = Postlike_Serializer
    permission_classes = [IsAuthenticated]
    def get(self, request, post_id):
        print(post_id)
        queryset = Post_like.objects.filter(post_id=post_id)
        serializer_class = Postlike_Serializer
        permission_classes = [IsAuthenticated]
        serializer = Postlike_Serializer(data = queryset)
        return Response(data,status=status.HTTP_200_OK)




























    #     queryset = Post_like.objects.all()
    #     serializer_class = Postlike_Serializer
    #     permission_classes = [IsAuthenticated]
    #     data = request.data
    #     data['total_likes'] = Post_like.objects.filter(user_id=request.user.pk).count()
        
    #     print(data)
    #     return Response({'data':data},status= status.HTTP_200_OK)


# class PostLike_View(ListCreateAPIView):
#     queryset = Post_like.objects.all()
#     serializer_class = Postlike_Serializer
#     permission_classes = [IsAuthenticated]
#     def create(self, request, *args, **kwargs):
#         data = request.data
#         # data['user_id'] = request.user_id
#         print(data)
        
#         serializer = Postlike_Serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Post Liked'},status= status.HTTP_201_CREATED)
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         data = request.data
#         data['total_likes'] = Post_like.objects.filter(user_id=request.user.pk).count()
        
#         print(data)
#         return Response({'data':data},status= status.HTTP_200_OK)



    

