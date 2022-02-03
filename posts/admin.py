from django.contrib import admin
from .models import Posts,Post_likes
# Register your models here.
@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','image','total_likes','total_comments','created_at']
    
@admin.register(Post_likes)
class PostLikesAdmin(admin.ModelAdmin):
    list_display = ['user_id','post_id','created_at']
