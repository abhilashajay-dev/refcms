# Generated by Django 3.2.11 on 2022-03-05 08:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flex', '0009_sectionstandardpage_standardpage_standardpagewithrawcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='authors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
