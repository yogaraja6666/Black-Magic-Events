# Generated by Django 4.2 on 2023-05-02 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_platinumcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platinumcart',
            name='ticketprice',
        ),
    ]
