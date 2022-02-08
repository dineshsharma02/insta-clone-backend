from django.urls import path
from . import views

urlpatterns = [
    
    path('postimage/',views.PostView.as_view(),name='postimage'),
    path('likepost/',views.PostLike_View.as_view(),name='likepost'),
    path('likepost/<int:post_id>/',views.PostItem_Like.as_view(),name='viewlikedpost'),

]