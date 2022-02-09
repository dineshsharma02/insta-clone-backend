from csv import list_dialects
from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import UserFollower

@admin.register(UserFollower)

class UserFollowerAdmin(admin.ModelAdmin):
    list_display = ['user_id','follower_id','created_at']

