# Generated by Django 3.0.2 on 2020-01-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20200119_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]