from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from postulant.permissions import IsPostulant
from .models import WorkDay, WorkModality, WorkExperience, JobRole, WorkArea
from .serializers import WorkModalitySerializer, JobRoleSerializer, \
    WorkAreaSerializer, WorkExperienceSerializer, WorkDaySerializer, PostulateToJobRegisterSerializer, \
    PostulateToJobSerializer


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


class PostulateToJob(APIView):
    permission_classes = (IsPostulant)

    def post(self, request):
        serializer = PostulateToJobRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        postulate = serializer.save()
        serializer_data = PostulateToJobSerializer(postulate)
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)
