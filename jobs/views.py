from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from companies.permissions import IsCompany
from .models import WorkDay, WorkModality, WorkExperience, JobRole, WorkArea, Job
from .serializers import WorkModalitySerializer, JobRoleSerializer, \
    WorkAreaSerializer, WorkExperienceSerializer, WorkDaySerializer, CreateJobterSerializer, JobSerializer, \
    JobPublicSerializer


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


class RegisterJobView(CreateAPIView):
    permission_classes = (IsCompany,)
    queryset = Job.objects.none()
    serializer_class = CreateJobterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        job = Job.objects.create(company=request.user.company, **serializer.data)
        serializer_data = JobSerializer(job)
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)


class JobsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        jobs = Job.objects.filter(is_active=True)
        serializer = JobPublicSerializer(jobs, many=True)
        return Response(serializer.data)
