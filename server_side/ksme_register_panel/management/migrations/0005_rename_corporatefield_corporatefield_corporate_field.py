# Generated by Django 3.2.5 on 2021-07-31 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corporatefield',
            old_name='corporateField',
            new_name='corporate_field',
        ),
    ]
