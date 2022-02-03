from django.urls import path
from . import views

urlpatterns = [
    
    path('postimage/',views.PostView.as_view(),name='postimage')

]