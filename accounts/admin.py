from csv import list_dialects
from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import UserFollower,Profile

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['id','username','bio','profile_pic']


@admin.register(UserFollower)

class UserFollowerAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','follower_id','created_at',"follow_status"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']
