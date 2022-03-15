from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SignUpCompanyApiView, SignInCompanyApiView
from django.contrib.auth.views import LogoutView

# router = DefaultRouter()
# router.register('signup', SignUpCompanyApiView)

urlpatterns = [
    path('api/auth/company/signup', SignUpCompanyApiView.as_view(), name="company_signup"),
    path('api/auth/company/signin', SignInCompanyApiView.as_view(), name="company_signin"),

    ## Empresa
]
