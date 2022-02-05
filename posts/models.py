
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# class InstaUser(models.Model):
#     # newname = User.first_name+" "User.last_name
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60,default=User.first_name)
    
#     email = models.EmailField(max_length=254,default=User.email)


# Create your models here.
class Posts(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    image = models.ImageField(upload_to='media/profpics/',default=None)
    caption = models.CharField(max_length=120,default="")
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Post_likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    post_id = models.ForeignKey("posts.Posts", on_delete=models.CASCADE,related_name='post_id',default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user_id','post_id')

    


# class Tags(models.Model):
#     tagged = models.ForeignKey(User,default=None)


# class Post_Comments(models.Model):
#     comment_to = models.ForeignKey(User,default=Posts.user)
#     comment_by = models.ForeignKey