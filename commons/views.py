# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from commons.models import Gender, DocumentType, Country, Region, SubRegion, District
from commons.serializers import GenderSerializer, DocumentTypeSerializer, CountrySerializer, RegionSerializer, \
    SubRegionSerializer, DistrictSerializer

from rest_framework import viewsets


class GenderListViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.filter(is_active=True)
    serializer_class = GenderSerializer


class DocumentTypeView(viewsets.ModelViewSet):
    queryset = DocumentType.objects.filter(is_active=True)
    serializer_class = DocumentTypeSerializer


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class SubRegionView(viewsets.ModelViewSet):
    queryset = SubRegion.objects.all()
    serializer_class = SubRegionSerializer


class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class UbigeoCountryView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        countries = Country.objects.filter()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class UbigeoRegionView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        regions = Region.objects.filter(country_id=pk)
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)


class UbigeoSubRegionView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        sub_regions = SubRegion.objects.filter(region_id=pk)
        serializer = SubRegionSerializer(sub_regions, many=True)
        return Response(serializer.data)


class UbigeoDistricView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        districts = District.objects.filter(subregion_id=pk)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)
