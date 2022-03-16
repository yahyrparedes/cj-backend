# Generated by Django 4.0.3 on 2022-03-16 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0001_initial'),
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Puesto de Trabajo',
                'verbose_name_plural': 'Puesto de Trabajo',
            },
        ),
        migrations.CreateModel(
            name='WorkArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Area de Trabajo',
                'verbose_name_plural': 'Area de Trabajo',
            },
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Jornada Laboral',
                'verbose_name_plural': 'Jornada Laboral',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Experiencia Laboral',
                'verbose_name_plural': 'Experiencia Laboral',
            },
        ),
        migrations.CreateModel(
            name='WorkModality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Modalidad de Trabajo',
                'verbose_name_plural': 'Modalidad de Trabajo',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=254)),
                ('benefit', models.TextField(max_length=254)),
                ('requirements', models.TextField(max_length=254)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.address')),
                ('job_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.jobrole')),
                ('work_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.workarea')),
                ('work_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.workexperience')),
                ('work_modality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.workmodality')),
                ('workday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.workday')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='RUC')),
                ('business_name', models.CharField(max_length=250, verbose_name='Razon Social')),
                ('tradename', models.CharField(max_length=250, verbose_name='Razon Social')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='Phone')),
                ('about', models.TextField(blank=True, verbose_name='Acerca de')),
                ('foundation_year', models.CharField(default='0000', max_length=4)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.address')),
                ('business_sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.businesssector')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]