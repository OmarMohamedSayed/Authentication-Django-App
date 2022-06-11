from django.urls import path
from .viewsets import *
from django.conf.urls import include

from rest_framework import routers
from django.conf.urls import include


router = routers.DefaultRouter()
router.register(r'profile', UserProfileView, basename='profile')


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('',include(router.urls)),
]