from django.contrib import admin
from .models import WorkDay, WorkModality, WorkExperience, JobRole, WorkArea, Job, Postulate


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active', 'created_at', 'updated_at')


@admin.register(WorkModality)
class WorkModalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active', 'created_at', 'updated_at')


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active', 'created_at', 'updated_at')


@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active', 'created_at', 'updated_at')


@admin.register(WorkArea)
class WorkAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active', 'created_at', 'updated_at')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'description', 'benefit', 'requirements')


@admin.register(Postulate)
class PostulateAreaAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'job', 'postulant', 'updated_at')
