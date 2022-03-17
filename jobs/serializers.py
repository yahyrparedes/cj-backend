from rest_framework import serializers

from commons.models import Address
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


class CreateJobterSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=254)
    description = serializers.CharField(required=True)
    benefit = serializers.CharField(required=True)
    requirements = serializers.CharField(required=True)
    workday = serializers.IntegerField(required=False)
    work_modality = serializers.IntegerField(required=False)
    work_experience = serializers.IntegerField(required=False)
    work_area = serializers.IntegerField(required=False)
    job_role = serializers.IntegerField(required=False)
    address = serializers.IntegerField(required=False)

    def validate_workday(self, value):
        if not WorkDay.objects.filter(pk=value).exists():
            raise serializers.ValidationError("WorkDay don't exist!")

    def validate_work_modality(self, value):
        if not WorkModality.objects.filter(pk=value).exists():
            raise serializers.ValidationError("WorkModality don't exist!")

    def validate_work_experience(self, value):
        if not WorkExperience.objects.filter(pk=value).exists():
            raise serializers.ValidationError("WorkExperience don't exist!")

    def validate_work_area(self, value):
        if not WorkArea.objects.filter(pk=value).exists():
            raise serializers.ValidationError("WorkArea don't exist!")

    def validate_job_role(self, value):
        if not JobRole.objects.filter(pk=value).exists():
            raise serializers.ValidationError("JobRole don't exist!")

    def validate_address(self, value):
        if not Address.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Address don't exist!")

    class Meta:
        model = Job
        fields = ('title', 'description', 'benefit', 'requirements',
                  'workday', 'work_modality', 'work_experience', 'work_area',
                  'job_role', 'address')


class JobSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'benefit', 'requirements',
                  'workday', 'work_modality', 'work_experience', 'work_area',
                  'job_role', 'address', 'is_active')
