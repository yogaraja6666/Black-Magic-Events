# Generated by Django 4.2 on 2023-04-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_myprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='bio',
        ),
        migrations.AddField(
            model_name='myprofile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='gender',
            field=models.CharField(default='Male', max_length=250),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='update_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]