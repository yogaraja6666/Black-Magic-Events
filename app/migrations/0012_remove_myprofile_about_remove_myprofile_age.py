# Generated by Django 4.2 on 2023-04-29 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_myprofile_bio_myprofile_about_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='age',
        ),
    ]