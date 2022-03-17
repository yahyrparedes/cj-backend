from django.urls import path, include
from .views import PostulantProfileView, SignUpPostulantApiView, SignInPostulantApiView, PostulateToJobView, \
    UploadCurriculumView

urlpatterns = [
    path('signup', SignUpPostulantApiView.as_view()),
    path('signin', SignInPostulantApiView.as_view()),
    path('profile', PostulantProfileView.as_view()),
    path('postulate', PostulateToJobView.as_view()),
    path('profile/upload-cv/<int:pk>/', UploadCurriculumView.as_view()),
]
