from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostulantProfileView, SignUpPostulantApiView, SignInPostulantApiView, PostulateToJobView

urlpatterns = [
    path('signup', SignUpPostulantApiView.as_view()),
    path('signin', SignInPostulantApiView.as_view()),
    path('profile', PostulantProfileView.as_view()),
    path('postulate', PostulateToJobView.as_view())
]
