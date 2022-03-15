from django.contrib import admin

# Register your models here.
from postulant.models import Postulant


@admin.register(Postulant)
class PostulantAdmin(admin.ModelAdmin):
    pass
