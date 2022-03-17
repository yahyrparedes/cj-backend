from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from commons.serializers import AddressSerializer
from users.models import User
from .models import Company, BusinessSector


class BusinessSectorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BusinessSector
        fields = '__all__'


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
        max_length=128
    )
    ruc = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Company.objects.all())],
        max_length=11
    )
    business_name = serializers.CharField(required=True)
    tradename = serializers.CharField(required=True)
    foundation_year = serializers.CharField(max_length=4, required=False)
    business_sector = serializers.IntegerField(required=False)
    phone = serializers.CharField(max_length=15, required=False)
    about = serializers.CharField(required=False)

    def to_representation(self, instance):
        # HACK: Overwrite User fields into the client instance to represent
        instance.email = instance.user.email
        instance.business_sector = instance.business_sector.id

        return super(SignUpCompanySerializer, self).to_representation(instance)

    class Meta:
        model = Company
        fields = ('id', 'email', 'password', 'ruc', 'business_name',
                  'tradename', 'foundation_year', 'business_sector',
                  'phone', 'about')


class CompanySerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = ('email', 'ruc', 'business_name', 'tradename',
                  'phone', 'business_sector', 'about', 'foundation_year',
                  'address', 'is_active', 'created_at',)


class CompanyPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('business_name', 'tradename', 'business_sector', 'address',)
