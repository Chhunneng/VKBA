# Generated by Django 2.2.2 on 2019-07-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_checkout_gift_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='estimate_date_receive',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
