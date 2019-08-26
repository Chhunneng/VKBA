# Generated by Django 2.2.2 on 2019-07-02 06:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0015_auto_20190305_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingmethod',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
