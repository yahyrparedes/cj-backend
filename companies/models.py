from django.conf import settings

from django.db import models

from commons.models import Address


class BusinessSector(models.Model):
    class Meta:
        verbose_name = 'Sector Empresarial'
        verbose_name_plural = 'Sector Empresarial'

    name = models.CharField(max_length=254)
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
        return str(self.name)


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
    phone = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=('Phone')
    )
    business_sector = models.ForeignKey(BusinessSector, on_delete=models.CASCADE, blank=True, null=True)
    about = models.TextField(
        blank=True,
        verbose_name=('Acerca de')
    )
    foundation_year = models.CharField(max_length=4, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
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

