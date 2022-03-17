from rest_framework import serializers

from postulant.models import Postulant
from postulant.serializer import PostulantSerializer
from .models import WorkDay, WorkModality, WorkExperience, WorkArea, JobRole, Postulate, Job


class WorkDaySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WorkDay
        fields = '__all__'


class WorkModalitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WorkModality
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WorkExperience
        fields = '__all__'


class WorkAreaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WorkArea
        fields = '__all__'


class JobRoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = JobRole
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    pass


class PostulateToJobRegisterSerializer(serializers.ModelSerializer):
    job = serializers.IntegerField(required=True)
    postulant = serializers.IntegerField(required=True)

    class Meta:
        model = Postulate
        fields = ('job', 'postulant')


class PostulateToJobSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    job = JobSerializer()
    postulant = PostulantSerializer()

    def validate_job(self, value):
        if not Job.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Job don't exist!")

    def validate_postulant(self, value):
        if not Postulant.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Postulant don't exist!")

    def save(self, **kwargs):
        postulant = Postulant.objects.create(**kwargs)
        return postulant

    class Meta:
        model = Postulate
        fields = ('id', 'job', 'postulant', 'is_active')
