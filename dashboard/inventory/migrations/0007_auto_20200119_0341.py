# Generated by Django 3.0.2 on 2020-01-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20200119_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sales_count',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
