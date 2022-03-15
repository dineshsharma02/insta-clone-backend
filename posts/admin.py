from django.contrib import admin
from .models import Post_Item,Post_like,Post_Comment
# Register your models here.
@admin.register(Post_Item)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','image','created_at']
    
@admin.register(Post_like)
class PostLikesAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','post_id','created_at']

@admin.register(Post_Comment)
class PostLikesAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','post_id','created_at','comment']

