# Generated by Django 3.2.5 on 2021-07-30 03:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skiils',
            new_name='Skills',
        ),
    ]
