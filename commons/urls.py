from django.urls import path, include
from rest_framework import routers

from .views import CountryView, RegionView, SubRegionView, DistrictView, DocumentTypeView, GenderListViewSet, \
    UbigeoCountryView, UbigeoRegionView, UbigeoSubRegionView, UbigeoDistricView

router = routers.DefaultRouter()
router.register('gender', GenderListViewSet)
router.register('document', DocumentTypeView)
router.register('country', CountryView)
router.register('region', RegionView)
router.register('subregion', SubRegionView)
router.register('district', DistrictView)

urlpatterns = [
    path('', include(router.urls)),
    path('ubigeo/country/', UbigeoCountryView.as_view()),
    path('ubigeo/country/<pk>/', UbigeoRegionView.as_view()),
    path('ubigeo/country/region/<pk>/', UbigeoSubRegionView.as_view()),
    path('ubigeo/country/region/subregion/<pk>/', UbigeoDistricView.as_view()),
]
