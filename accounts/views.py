from rest_framework import views
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .serializer import  RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

# class LoginView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = LoginSerializer
#     authentication_classes = [BasicAuthentication,SessionAuthentication]
#     permission_classes = [IsAuthenticated]
    
# class LoginView(views.APIView):
#     def post(self,request,format=None):
#         data = request.data
#         username = data.get('username',None)
#         password = data.get('password',None)
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)

#                 return Response({'msg':'successfully loggedin'},status=status.HTTP_200_OK)
#             else:
#                 return Response({'msg':'Please Activate your account'},status=status.HTTP_404_NOT_FOUND)
#         else:
#  
#            return Response({'msg':'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)


class LoginView(views.APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content)
