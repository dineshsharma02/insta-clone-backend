
from django.urls import path,include
from rest_framework import routers
from accounts import views

router = routers.SimpleRouter()

# router.register('login/',views.LoginView.as_view(),basename='auth_login')

urlpatterns = [ 
    path('register/',views.RegisterView.as_view(),name='auth_register'),
    path('login/',views.LoginView.as_view(),name='auth_login')
    # path('',include(router.urls))
]
