# Generated by Django 3.0.2 on 2020-01-23 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20200122_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='lon',
            new_name='long',
        ),
    ]
