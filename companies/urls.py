from django.urls import path
from .views import SignUpCompanyApiView, SignInCompanyApiView, CompanyProfileView

urlpatterns = [
    path('signup', SignUpCompanyApiView.as_view()),
    path('signin', SignInCompanyApiView.as_view()),
    path('profile', CompanyProfileView.as_view()),
]
