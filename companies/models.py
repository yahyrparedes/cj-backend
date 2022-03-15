from django.conf import settings
from django.utils.translation import gettext as _

from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.RESTRICT)
    ruc = models.CharField(
        max_length=11,
        verbose_name=('RUC'),
        unique=True
    )
    business_name = models.CharField(
        max_length=250,
        verbose_name=('Razon Social')
    )
    tradename = models.CharField(
        max_length=250,
        verbose_name=('Razon Social')
    )
    description = models.TextField(
        blank=True,
        verbose_name=('Description')
    )
    phone = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=('Phone')
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=('Address')
    )
    is_active = models.BooleanField(default=True, verbose_name=("Is active"))
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Updated At")
    )

    def __str__(self):
        return str(self.user)
