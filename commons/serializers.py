# Django Rest Framework
from rest_framework import serializers

from .models import Gender, DocumentType, Country, Region, SubRegion, District


class GenderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Gender
        fields = ('id', 'short_name', 'long_name')


class DocumentTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = DocumentType
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ['id']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        read_only_fields = ['id']


class SubRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRegion
        fields = '__all__'
        read_only_fields = ['id']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        read_only_fields = ['id']


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    country = CountrySerializer()
    region = RegionSerializer()
    sub_region = SubRegionSerializer()
    DistrictSerializer = DistrictSerializer()

    class Meta:
        model = Gender
        fields = ('id', 'name', 'reference', 'country', 'region',
                  'sub_region', 'district')
