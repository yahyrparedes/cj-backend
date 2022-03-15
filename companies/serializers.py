from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from users.models import User
from .models import Company


class SignUpCompanySerializer(serializers.ModelSerializer):
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
    ruc = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Company.objects.all())],
        max_length=11
    )
    business_name = serializers.CharField(required=True)
    tradename = serializers.CharField(required=True)
    description = serializers.CharField(required=False)

    def to_representation(self, instance):
        # HACK: Overwrite User fields into the client instance to represent
        instance.email = instance.user.email
        return super(SignUpCompanySerializer, self).to_representation(instance)

    class Meta:
        model = Company
        fields = ('id', 'email', 'password', 'ruc',
                  'business_name', 'tradename', 'description')


class CompanySerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Company
        fields = ('ruc', 'business_name', 'tradename', 'created_at', 'email',
                  'description', 'phone', 'address', 'is_active')
