from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from authentication.serializers import AuthTokenSerializer
from jobs.models import Job
from jobs.serializers import JobSerializer
from users.models import User
from .models import Company, BusinessSector
from .permissions import IsCompany
from .serializers import SignUpCompanySerializer, CompanySerializer, BusinessSectorSerializer


class BusinessSectorViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = BusinessSector.objects.filter(is_active=True)
    serializer_class = BusinessSectorSerializer


class SignInCompanyApiView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            courier_serializer = CompanySerializer(user.company)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'auth_token': token.key, 'company': courier_serializer.data})
        except Company.DoesNotExist:
            raise PermissionDenied


class SignUpCompanyApiView(CreateAPIView):
    queryset = Company.objects.none()
    permission_classes = (AllowAny,)
    serializer_class = SignUpCompanySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        company = self.create_company(validated_data)
        return self.login_and_response(company)

    def login_and_response(self, client):
        client_data = CompanySerializer(
            instance=client, context={'user': client.user}
        ).data
        token, _ = Token.objects.get_or_create(user=client.user)
        return Response(
            {'auth_token': token.key, 'company': client_data},
            status=status.HTTP_201_CREATED
        )

    def create_company(self, data):
        user_data = {
            'email': data.pop('email'),
            'password': data.pop('password')
        }

        user = User.objects.create_user(**user_data)
        company = Company.objects.create(
            user=user, is_active=True, **data
        )
        return company


class CompanyProfileView(RetrieveUpdateAPIView):
    model = Company
    serializer_class = CompanySerializer
    permission_classes = (IsCompany,)

    def get_object(self, *args, **kwargs):
        return self.request.user.company


class CompanyJobsView(APIView):
    permission_classes = (IsCompany,)

    def get(self, requests):
        jobs = Job.objects.filter(company=requests.user.company)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
