from django.db.models.signals import post_save
from tokenize import Token
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class UserFollower(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id')
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id','follower_id')