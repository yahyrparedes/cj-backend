from rest_framework import serializers
from .models import WorkDay, WorkModality, WorkExperience, WorkArea, JobRole


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
