from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from jobs.models import Postulate, Job
from jobs.serializers import JobSerializer
from postulant.models import Curriculum, Postulant
from users.models import User


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = (
            'pk',
            'name',
            'name_original',
            'format',
            'url'
        )


class SignUpPostulantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        required=True,
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        validators=[validate_password],
        write_only=True,
        max_length=128, )
    name = serializers.CharField(required=True, max_length=254)
    last_name = serializers.CharField(required=True, max_length=254)

    def to_representation(self, instance):
        # HACK: Overwrite User fields into the client instance to represent
        instance.email = instance.user.email
        instance.name = instance.user.first_name
        instance.last_name = instance.user.last_name
        return super(SignUpPostulantSerializer, self).to_representation(instance)

    class Meta:
        model = Postulant
        fields = ('id', 'email', 'password', 'name', 'last_name',)


class PostulantSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    curriculum = CurriculumSerializer(read_only=True)
    curriculum_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Postulant
        # fields = ('gender', 'document_type', 'document', 'created_at', 'email',
        #           'date_of_birth', 'phone', 'is_active', 'avatar', 'name', 'last_name')
        fields = ('pk', 'gender', 'document_type', 'document', 'created_at', 'email',
                  'date_of_birth', 'phone', 'is_active', 'avatar', 'name', 'last_name', 'curriculum', 'curriculum_id')


class PostulateToJobRegisterSerializer(serializers.ModelSerializer):
    job = serializers.IntegerField(required=True)

    def validate_job(self, value):
        if not Job.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Job don't exist!")
        return value

    class Meta:
        model = Postulate
        fields = ('job',)


class PostulateToJobSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    job = JobSerializer()
    postulant = PostulantSerializer()

    class Meta:
        model = Postulate
        fields = ('id', 'job', 'postulant', 'is_active')
