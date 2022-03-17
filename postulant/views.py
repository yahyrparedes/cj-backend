from django.shortcuts import render

# Create your views here.
from rest_framework import status, parsers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import AuthTokenSerializer
from jobs.models import Postulate, Job
from jobs.serializers import JobSerializer
from postulant.serializer import PostulateToJobRegisterSerializer, \
    PostulateToJobSerializer

from postulant.models import Curriculum, Postulant
from postulant.permissions import IsPostulant, IsAuthenticated
from postulant.serializer import CurriculumSerializer, PostulantSerializer, SignUpPostulantSerializer

from users.models import User
import cloudinary.uploader


class SignInPostulantApiView(APIView):
    serializer_class = AuthTokenSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            postulant_serializer = PostulantSerializer(user.postulant)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'auth_token': token.key, 'postulant': postulant_serializer.data})
        except Postulant.DoesNotExist:
            raise PermissionDenied


class SignUpPostulantApiView(CreateAPIView):
    queryset = Postulant.objects.none()
    permission_classes = (AllowAny,)
    serializer_class = SignUpPostulantSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        company = self.create_postulant(validated_data)
        return self.login_and_response(company)

    def login_and_response(self, client):
        client_data = PostulantSerializer(
            instance=client, context={'user': client.user}
        ).data
        token, _ = Token.objects.get_or_create(user=client.user)
        return Response(
            {'auth_token': token.key, 'postulant': client_data},
            status=status.HTTP_201_CREATED
        )

    def create_postulant(self, data):
        user_data = {
            'email': data.pop('email'),
            'password': data.pop('password'),
            'first_name': data.pop('name'),
            'last_name': data.pop('last_name')
        }

        user = User.objects.create_user(**user_data)
        postulant = Postulant.objects.create(
            user=user, is_active=True, **data
        )
        return postulant


class PostulantProfileView(RetrieveUpdateAPIView):
    model = Postulant
    serializer_class = PostulantSerializer
    permission_classes = (AllowAny,)

    def get_object(self, *args, **kwargs):
        return self.request.user.postulant


class PostulateToJobView(CreateAPIView):
    permission_classes = (IsPostulant,)
    queryset = Postulant.objects.none()
    serializer_class = PostulateToJobRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        postulant = Postulate.objects.create(job_id=serializer.data.get('job'), postulant=request.user.postulant)
        serializer_data = PostulateToJobSerializer(postulant)
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)


class UploadCurriculumView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def patch(request, pk):

        file = request.data.get('cv')
        upload_data = cloudinary.uploader.upload(file)

        curriculum = CurriculumSerializer(data={
            "name": upload_data.get('public_id'),
            "name_original": upload_data.get('original_filename'),
            "format": upload_data.get('format'),
            "url": upload_data.get('url')
        })

        if curriculum.is_valid():
            curriculum.save()

        curriculum_id = Curriculum.objects.filter(pk=int(curriculum.data.get('pk'))).first()

        postulant = Postulant.objects.get(pk=pk)
        postulant_file = {
            "curriculum_id": curriculum_id.id
        }
        postulantSerializer = PostulantSerializer(postulant, data=postulant_file, partial=True)
        if postulantSerializer.is_valid():
            postulantSerializer.save()

        return Response({
            'status': 'success',
            'data': postulantSerializer.data
        }, status=201)


class PostulantJobsView(APIView):
    permission_classes = (IsPostulant,)

    def get(self, request, *args, **kwargs):
        jobs = Postulate.objects.filter(is_active=True, postulant=request.user.postulant)
        serializer = PostulateToJobSerializer(jobs, many=True)
        return Response(serializer.data)
