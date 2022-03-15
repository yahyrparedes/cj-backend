from django.db import models
from django.utils.translation import gettext as _

from crum import get_current_user
# Create your models here.

class ConsoleJobsAbstractClass(models.Model):
    class Meta:
        verbose_name = "ConsoleJobs Abstract Class"
        abstract = True

    is_active = models.BooleanField(
        default=True,
        verbose_name=("Is active")
    )
    created = models.DateField(
        auto_now=True,
        verbose_name=("Created")
    )
    updated = models.DateField(
        auto_now=True,
        verbose_name=("Updated")
    )
    updated_by = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )
    created_by = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user

        super(ConsoleJobsAbstractClass, self).save(*args, **kwargs)

    def delete(self):
        self.is_active = False
        self.save()


class Gender(models.Model):
    short_name = models.CharField(max_length=5, )
    long_name = models.CharField(max_length=100, )
    is_active = models.BooleanField(default=True, )

    def __str__(self):
        return self.long_name


class DocumentType(models.Model):
    long_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=55)
    character_length = models.SmallIntegerField()
    type_character = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name


class Faq(models.Model):
    question = models.CharField(max_length=255),
    answer = models.TextField(),
    is_active = models.BooleanField(
        default=True,
        verbose_name=("Is active")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Updated At")
    )


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to="core/static/images/category/",
        default='core/static/images/category/default.png',
    )
    father = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_active = models.BooleanField(
        default=True,
        verbose_name=("Is active")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Updated At")
    )


class BasePlace(models.Model):
    name = models.CharField(
        _('Nombre'),
        max_length=30
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{0}".format(self.name)


class BaseUbigeoPlace(BasePlace):
    ubigeo_code = models.IntegerField(
        _('Codigo de ubigeo'),
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Country(BasePlace):
    alpha2code = models.CharField(
        _('Codigo de 2 letras'),
        max_length=2,
        unique=True
    )
    alpha3code = models.CharField(
        _('Codigo de 3 letras'),
        max_length=3,
        unique=True
    )
    numeric_code = models.IntegerField(
        _('Codigo numerico'),
        unique=True
    )
    phone_prefix = models.IntegerField(
        _('Prefijo telefonico'),
        unique=True,
        default=0
    )

    class Meta:
        verbose_name = _('Pais')
        verbose_name_plural = _('Paises')


class CountryCodePhone(Country):
    class Meta:
        proxy = True

    def __str__(self):
        return "{0}".format(self.phone_prefix)


class Region(BaseUbigeoPlace):
    country = models.ForeignKey(
        Country,
        verbose_name=_('Pais'),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')


class SubRegion(BaseUbigeoPlace):
    region = models.ForeignKey(
        Region,
        verbose_name=_('Regiones'),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')


class District(BaseUbigeoPlace):
    subregion = models.ForeignKey(
        SubRegion,
        verbose_name=_('Provincia'),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _('Distrito')
        verbose_name_plural = _('Distritos')
