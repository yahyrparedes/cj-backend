from rest_framework import routers
from .views import UserView, CustomAuthToken

from django.urls import path
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('api/v1/user/<pk>/', UserView.as_view()),
    path('api/v1/signin/', CustomAuthToken.as_view(), name="signin"),
    # path('api/v1/signup/', CustomCreateUser.as_view(), name="signup"),
]
