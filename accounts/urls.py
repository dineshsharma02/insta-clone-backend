
from django.urls import path,include
from rest_framework import routers
from accounts import views

router = routers.SimpleRouter()

router.register('',views.AccountViewSet,basename='accounts')

urlpatterns = [ 
    path('',include(router.urls))
]
