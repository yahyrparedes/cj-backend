from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import WorkDay, WorkModality, WorkExperience, JobRole, WorkArea
from .serializers import WorkModalitySerializer, JobRoleSerializer, \
    WorkAreaSerializer, WorkExperienceSerializer, WorkDaySerializer


class WorkDayViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = WorkDay.objects.filter(is_active=True)
    serializer_class = WorkDaySerializer


class WorkModalityViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = WorkModality.objects.filter(is_active=True)
    serializer_class = WorkModalitySerializer


class WorkExperienceViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = WorkExperience.objects.filter(is_active=True)
    serializer_class = WorkExperienceSerializer


class WorkAreaViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = WorkArea.objects.filter(is_active=True)
    serializer_class = WorkAreaSerializer


class JobRoleViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = JobRole.objects.filter(is_active=True)
    serializer_class = JobRoleSerializer
