from django.urls import path, include
from rest_framework import routers

from .views import SignUpCompanyApiView, SignInCompanyApiView, CompanyProfileView, BusinessSectorViewSet, \
    CompanyJobsView

router = routers.DefaultRouter()
router.register('bussiness', BusinessSectorViewSet)

urlpatterns = [
    path('commons/', include(router.urls)),
    path('signup', SignUpCompanyApiView.as_view()),
    path('signin', SignInCompanyApiView.as_view()),
    path('profile', CompanyProfileView.as_view()),
    path('jobs', CompanyJobsView.as_view())
]
