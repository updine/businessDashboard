# Generated by Django 3.0.2 on 2020-01-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20200122_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]