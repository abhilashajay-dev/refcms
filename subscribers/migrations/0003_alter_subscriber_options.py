# Generated by Django 3.2.11 on 2022-03-16 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_rename_subcribers_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Subscriber', 'verbose_name_plural': 'Subscribers'},
        ),
    ]
