from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostulantProfileView, SignUpPostulantApiView, SignInPostulantApiView
from django.contrib.auth.views import LogoutView

# router = DefaultRouter()
# router.register('signup', SignUpCompanyApiView)

urlpatterns = [
    path('api/postulant/signup', SignUpPostulantApiView.as_view() ),
    path('api/postulant/signin', SignInPostulantApiView.as_view() ),

    path('api/postulant/profile', PostulantProfileView.as_view()),

    ## Empresa
]
