from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostulantProfileView, SignUpPostulantApiView, SignInPostulantApiView, UploadCurriculumView

urlpatterns = [
    path('signup', SignUpPostulantApiView.as_view()),
    path('signin', SignInPostulantApiView.as_view()),
    path('profile', PostulantProfileView.as_view()),
    path('profile/upload-cv/<int:pk>/', UploadCurriculumView.as_view()),
]
