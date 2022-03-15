from django.db import models
from django.conf import settings

# Create your models here.
from django.utils.functional import cached_property

from commons.models import Gender, DocumentType
from users.models import User


class Postulant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,
                                on_delete=models.RESTRICT)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, blank=True, null=True)
    document = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to="core/static/images/avatar/",
        default='core/static/images/avatar/default.jpeg',
    )
    phone = models.CharField(max_length=20, blank=True)
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

    @cached_property
    def full_name(self):
        return self.user.get_full_name()

    def _gender(self):
        return self.gender.long_name

    def _document_type(self):
        return self.document_type.short_name

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
