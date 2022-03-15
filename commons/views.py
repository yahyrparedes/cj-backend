# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.commons.models import Gender, DocumentType, Country, Region, SubRegion, District
from apps.commons.serializers import GenderSerializer, DocumentTypeSerializer, CountrySerializer, RegionSerializer, \
    SubRegionSerializer, DistrictSerializer

from rest_framework import viewsets


class GenderListView(APIView):

    # GET
    def get(self, request):
        gender = Gender.objects.filter(is_active=True)  # QuerySet
        serializer = GenderSerializer(gender, many=True)  # Many=lista=muchos
        return Response(serializer.data)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


# class DocumentTypeListView(APIView):
#     def get(self, request):
#         # document_type = DocumentType.objects.all()
#         document_type = DocumentType.objects.filter(is_active=True)
#         serializer = DocumentTypeSerializer(document_type, many=True)
#         return Response(serializer.data)

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


# GET  country/ -> lista de paises
# POST country/ -> registro
# PUT  country/{id}/  -> actualizar un elemento
# GET  country/{id}/  -> detalle de un elemento
# DELETE country/{id}/ -> eliminar elimancion - fisica


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
