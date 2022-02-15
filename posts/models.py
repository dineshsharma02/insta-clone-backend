from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile


class Post_Item(models.Model):
    # post_id = models.AutoField(primary_key=True)
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    # prof_pic = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # username = models.CharField(max_length=255,default="anonuser")
    image = models.ImageField(upload_to='media/profpics/',default=None)
    caption = models.CharField(max_length=120,default="")
    total_likes = models.IntegerField(default=10)
    total_comments = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

class Post_like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user',blank=False)
    post_id = models.ForeignKey(Post_Item, on_delete=models.CASCADE,related_name='postid',default=None,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user_id','post_id')

class Post_Comment(models.Model):
    post_id = models.ForeignKey(Post_Item, on_delete=models.CASCADE,default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     unique_together = ('user_id','post_id')


    


# class Tags(models.Model):
#     tagged = models.ForeignKey(User,default=None)


# class Post_Comments(models.Model):
#     comment_to = models.ForeignKey(User,default=Posts.user)
#     comment_by = models.ForeignKey