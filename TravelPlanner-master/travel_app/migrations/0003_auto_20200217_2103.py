# Generated by Django 2.2 on 2020-02-17 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_trip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='pw',
        ),
    ]
