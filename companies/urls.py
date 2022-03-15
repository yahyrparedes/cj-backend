from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SignUpCompanyApiView, SignInCompanyApiView, CompanyProfileView
from django.contrib.auth.views import LogoutView

# router = DefaultRouter()
# router.register('signup', SignUpCompanyApiView)

urlpatterns = [
    path('api/company/signup', SignUpCompanyApiView.as_view() ),
    path('api/company/signin', SignInCompanyApiView.as_view() ),

    path('api/company/profile', CompanyProfileView.as_view()),

    ## Empresa
]
