from django.contrib import admin

# Register your models here.
from companies.models import Company, BusinessSector


@admin.register(BusinessSector)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'ruc', 'business_name', 'tradename', 'is_active')
