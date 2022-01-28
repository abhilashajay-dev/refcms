# Generated by Django 3.2.11 on 2022-01-28 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'flex page',
                'verbose_name_plural': 'flex pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
