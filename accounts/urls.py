
from django.urls import path,include
from rest_framework import routers
from accounts import views

router = routers.SimpleRouter()

# router.register('login/',views.LoginView.as_view(),basename='auth_login')

urlpatterns = [ 
    path('register/',views.RegisterView.as_view(),name='auth_register'),
    path('login/',views.LoginView.as_view(),name='auth_login'),
    path('userprofile/<int:pk>/',views.Profile_View.as_view(),name='user_profile'),
    path('userprofile/',views.Profile_View_List.as_view(),name='user_profile')
    # path('',include(router.urls))
]
