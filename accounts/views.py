from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .serializer import  RegistrationSerializer
from django.contrib.auth.models import User
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
