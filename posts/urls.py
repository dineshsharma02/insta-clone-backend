from django.urls import path
from . import views

urlpatterns = [
    
    path('postimage/',views.PostView.as_view(),name='postimage'),
    path('likepost/',views.PostItem_Like.as_view(),name='likepost'),
    path('commentpost/',views.PostItem_Comment_View.as_view(),name='commentpost'),
    path('likepost/<int:post_id>/',views.PostItem_Like.as_view(),name='viewlikedpost'),
    path('delpostlike/<int:post_id>/<int:user_id>/',views.PostItem_Like_Del.as_view(),name='viewlikedpostdel'),
    path('userposts/',views.User_Posts_View.as_view(),name="userpostview"),
    path('userposts/<int:user_id>/',views.User_Posts_View.as_view(),name="userpost"),

]