# Generated by Django 4.2 on 2023-04-15 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_levent1_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='pnumber',
            new_name='phonenumber',
        ),
    ]