from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from .managers import UserManager
from commons.models import Gender, DocumentType


class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(
        verbose_name='Email Address',
        help_text=_('Correo electronico'),
        max_length=255,
        unique=True, )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

