from django.db import models

# Create your models here.
from commons.models import Address
from postulant.models import Postulant


class WorkDay(models.Model):
    class Meta:
        verbose_name = 'Jornada Laboral'
        verbose_name_plural = 'Jornada Laboral'

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


class WorkModality(models.Model):
    class Meta:
        verbose_name = 'Modalidad de Trabajo'
        verbose_name_plural = 'Modalidad de Trabajo'

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


class WorkExperience(models.Model):
    class Meta:
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencia Laboral'

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


class WorkArea(models.Model):
    class Meta:
        verbose_name = 'Area de Trabajo'
        verbose_name_plural = 'Area de Trabajo'

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


class JobRole(models.Model):
    class Meta:
        verbose_name = 'Puesto de Trabajo'
        verbose_name_plural = 'Puesto de Trabajo'

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


class Job(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    benefit = models.TextField(max_length=254)
    requirements = models.TextField(max_length=254)
    workday = models.ForeignKey(WorkDay, on_delete=models.CASCADE)
    work_modality = models.ForeignKey(WorkModality, on_delete=models.CASCADE)
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    work_area = models.ForeignKey(WorkArea, on_delete=models.CASCADE)
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)


class Postulate(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE),
    postulant = models.ForeignKey(Postulant, on_delete=models.CASCADE)
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
        return f'{self.postulant} {self.job}'
