from django.urls import path, include
from rest_framework import routers

from .views import WorkDayViewSet, WorkModalityViewSet, WorkExperienceViewSet, WorkAreaViewSet, JobRoleViewSet, \
    RegisterJobView

router = routers.DefaultRouter()
router.register('workday', WorkDayViewSet)
router.register('modality', WorkModalityViewSet)
router.register('experience', WorkExperienceViewSet)
router.register('area', WorkAreaViewSet)
router.register('role', JobRoleViewSet)

urlpatterns = [
    path('commons/', include(router.urls)),
    path('create/', RegisterJobView.as_view()),
]
