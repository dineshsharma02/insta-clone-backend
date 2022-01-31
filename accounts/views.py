from django.shortcuts import render
from rest_framework import viewsets

from .serializer import  UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
