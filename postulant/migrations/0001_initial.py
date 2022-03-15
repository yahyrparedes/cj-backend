# Generated by Django 4.0.3 on 2022-03-15 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('document', models.CharField(max_length=15, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(default='core/static/images/avatar/default.jpeg', upload_to='core/static/images/avatar/')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.documenttype')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.gender')),
            ],
        ),
    ]
