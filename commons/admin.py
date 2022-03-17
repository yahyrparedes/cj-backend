from django.contrib import admin

# Register your models here.
from .models import Gender, DocumentType, Country, Region, SubRegion, District


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('long_name', 'short_name', 'is_active')


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('long_name', 'short_name', 'character_length', 'type_character', 'is_active')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'alpha2code',
        'alpha3code',
        'numeric_code',
        'phone_prefix',
    ]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'ubigeo_code',
        'country'
    ]


@admin.register(SubRegion)
class SubRegionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'ubigeo_code',
        'region',
    ]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'ubigeo_code',
        'subregion',
    ]
