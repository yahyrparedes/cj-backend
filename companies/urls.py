from django.urls import path, include
from rest_framework import routers

from .views import SignUpCompanyApiView, SignInCompanyApiView, CompanyProfileView, BusinessSectorViewSet, \
    CompanyViewSet, WorkDayViewSet, WorkModalityViewSet, WorkExperienceViewSet, WorkAreaViewSet, JobRoleViewSet

router = routers.DefaultRouter()
router.register('bussiness', BusinessSectorViewSet)
router.register('workday', WorkDayViewSet)
router.register('modality', WorkModalityViewSet)
router.register('experience', WorkExperienceViewSet)
router.register('area', WorkAreaViewSet)
router.register('role', JobRoleViewSet)

urlpatterns = [
    path('commons/', include(router.urls)),
    path('signup', SignUpCompanyApiView.as_view()),
    path('signin', SignInCompanyApiView.as_view()),
    path('profile', CompanyProfileView.as_view()),
]
