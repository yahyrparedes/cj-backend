from rest_framework import routers

from views import CountryView, RegionView, SubRegionView, DistrictView, DocumentTypeViewSet

router = routers.DefaultRouter()
router.register('document', DocumentTypeViewSet)
router.register('country', CountryView)
router.register('region', RegionView)
router.register('subregion', SubRegionView)
router.register('district', DistrictView)
urlpatterns = router.urls
