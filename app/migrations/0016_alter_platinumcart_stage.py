# Generated by Django 4.2 on 2023-05-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_platinumcart_stage_platinumcart_ticketprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platinumcart',
            name='stage',
            field=models.CharField(default='Platinum Stage', max_length=500),
        ),
    ]
