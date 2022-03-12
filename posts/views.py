

from xml.dom import NotFoundErr
from django.http import QueryDict
from django.shortcuts import render
from numpy import generic
from .serializer import PostSerializerImageField,Postlike_Serializer,Post_Comment_Serializer,User_Post_Details_Serializer
from rest_framework import viewsets
from .models import Post_Item,Post_like,Post_Comment
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveDestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from posts import serializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User



############### SENDS POST INFO #############################

class PostView(ListCreateAPIView):
    queryset = Post_Item.objects.all()
    serializer_class = PostSerializerImageField
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        
        data['user_id'] = request.user.id
        print(data)
        serializer = PostSerializerImageField(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


############### SHOWS ALL THE LIKES OF ALL POSTS BY ALL USER (NOT VERY USEFUL) ####################

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




######### FOR INDIVIDUAL LIKES ON THE POST #################

class PostItem_Like(ListCreateAPIView):
    queryset = Post_Item.objects.all()
    serializer_class = Postlike_Serializer
    permission_classes = [IsAuthenticated]
    def get(self, request, post_id=None):
        print(post_id)
        if (post_id):
            queryset = Post_like.objects.filter(post_id=post_id)
            serializer = Postlike_Serializer(queryset,many=True)
        else:
            queryset = Post_like.objects.all()
            serializer = Postlike_Serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):

        #############   ISSUE ----> WHEN TRY TO ADD USER_ID WHEN IT IS IN ITS READ_ONLY STATE IT DOESN'T ADD ENTRY WITH USER_ID ###############

        print("starting like")
        data = request.data.copy()
        print(request.data)
        data['user_id'] = '{user_id}'.format(user_id=request.user.pk)
        
        print(data)
        serializer = Postlike_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'post liked'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
class PostItem_Like_Del(RetrieveDestroyAPIView):
    queryset = Post_like.objects.all()
    serializer_class = Postlike_Serializer
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id=None,user_id=None):
        queryset = Post_like.objects.get(post_id=post_id,user_id=user_id)
        serializer = Postlike_Serializer(queryset)
        return Response(serializer.data)

    def delete(self, request, post_id=None):
        user_id = request.user.pk
        post_like = None
        try:
            post_like = Post_like.objects.filter(post_id=post_id,user_id=user_id)
        except(NotFoundErr):
            print("Not fonud")
        
        
        if post_like:
            post_like.delete()
            return Response({'msg':'post like removed'},status= status.HTTP_202_ACCEPTED)
        else:
            return Response({'msg':'post like not found'},status= status.HTTP_404_NOT_FOUND)

    def create(self,request,*args,**kwargs):

        #############   ISSUE ----> WHEN TRY TO ADD USER_ID WHEN IT IS IN ITS READ_ONLY STATE IT DOESN'T ADD ENTRY WITH USER_ID ###############

        print("starting like")
        data = request.data.copy().dict()
        print(data)
        data['user_id'] = '{user_id}'.format(user_id=request.user.pk)
        print(data)
        serializer = Postlike_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'post liked'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        


######################### SHOWS ALL COMMENTS #####################################

class PostItem_Comment_View(ListCreateAPIView):
    queryset = Post_Comment.objects.all()
    serializer_class = Post_Comment_Serializer
    permission_classes = [IsAuthenticated]
    # def create(self, request, *args, **kwargs):
    #     user_id = self.request.user
    def get(self, request, post_id=None):
        print(post_id)
        if (post_id):
            queryset = Post_Comment.objects.filter(post_id=post_id)
            serializer = Post_Comment_Serializer(queryset,many=True)
        else:
            queryset = Post_Comment.objects.all()
            serializer = Post_Comment_Serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):

        #############   ISSUE ----> WHEN TRY TO ADD USER_ID WHEN IT IS IN ITS READ_ONLY STATE IT DOESN'T ADD ENTRY WITH USER_ID ###############

        print("starting commetn")
        data = request.data.copy()
        print(request.data)
        data['user_id'] = '{user_id}'.format(user_id=request.user.pk)
        
        print(data)
        serializer = Post_Comment_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'commented on post'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        

class IsLiked(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,post_id=None):
        data = False
        user_id = request.user.pk
        if Post_like.objects.filter(post_id=post_id,user_id=user_id):
            data = True
            return Response(data,status = status.HTTP_200_OK)
        return Response(data,status=status.HTTP_404_NOT_FOUND)
























    #     queryset = Post_like.objects.all()
    #     serializer_class = Postlike_Serializer
    #     permission_classes = [IsAuthenticated]
    #     data = request.data
    #     data['total_likes'] = Post_like.objects.filter(user_id=request.user.pk).count()
        
    #     print(data)
    #     return Response({'data':data},status= status.HTTP_200_OK)


class PostLike_View(ListCreateAPIView):
    queryset = Post_like.objects.all()
    serializer_class = Postlike_Serializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        data = request.data
        # data['user_id'] = request.user_id
        print(data)
        
        serializer = Postlike_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Post Liked'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        data = request.data
        data['total_likes'] = Post_like.objects.filter(user_id=request.user.pk).count()
        
        print(data)
        return Response({'data':data},status= status.HTTP_200_OK)

# class User_Posts_View(ListAPIView):
#     # serializer_class = User_Post_Details_Serializer

#     # def get_queryset(self):
#     #     user = self.request.user
#     #     print(user)
#     #     return Post_Item.objects.filter(user_id = int(user))
    
#     queryset = Post_Item.objects.all()
    

#     def get(self, request, user_id=None):
#         # username = str(user_id)
#         if (user_id):
#             queryset = Post_Item.objects.filter(user_id=user_id)

#             serializer = User_Post_Details_Serializer(queryset,many=True)
            
#         else:
#             queryset = Post_Item.objects.all()
#             serializer = User_Post_Details_Serializer(queryset,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)


# class User_Posts_View(API):


class User_Posts_View(APIView):
    queryset = Post_Item.objects.all()
    serializer_class = User_Post_Details_Serializer
    # permission_classes = [IsAuthenticated]
    def get(self, request, username=None):
        # username = str(user_id)
        user_id = get_user_id(username)
        # print(user_id)
        # username = str(username)
        if (username):
            queryset = Post_Item.objects.filter(user_id=user_id)

            serializer = User_Post_Details_Serializer(queryset,many=True,context={"request":request})
            
        else:
            queryset = Post_Item.objects.all()
            serializer = User_Post_Details_Serializer(queryset,many=True,context={"request":request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    
def get_user_id(username=None):
    user_obj =  User.objects.get(username=username)
    user_id = user_obj.id
    return user_id