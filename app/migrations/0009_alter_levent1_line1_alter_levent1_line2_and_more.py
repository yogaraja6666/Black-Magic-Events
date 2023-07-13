# Generated by Django 4.2 on 2023-04-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_levent2_levent3_levent4_uevent1_uevent2_uevent3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levent1',
            name='line1',
            field=models.CharField(default='levent1', max_length=25),
        ),
        migrations.AlterField(
            model_name='levent1',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent1',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent2',
            name='line1',
            field=models.CharField(default='levent2', max_length=25),
        ),
        migrations.AlterField(
            model_name='levent2',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent2',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent3',
            name='line1',
            field=models.CharField(default='levent3', max_length=25),
        ),
        migrations.AlterField(
            model_name='levent3',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent3',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent4',
            name='line1',
            field=models.CharField(default='levent4', max_length=25),
        ),
        migrations.AlterField(
            model_name='levent4',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='levent4',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent1',
            name='line1',
            field=models.CharField(default='uevent1', max_length=25),
        ),
        migrations.AlterField(
            model_name='uevent1',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent1',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent2',
            name='line1',
            field=models.CharField(default='uevent2', max_length=25),
        ),
        migrations.AlterField(
            model_name='uevent2',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent2',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent3',
            name='line1',
            field=models.CharField(default='uevent3', max_length=25),
        ),
        migrations.AlterField(
            model_name='uevent3',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent3',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent4',
            name='line1',
            field=models.CharField(default='uevent4', max_length=25),
        ),
        migrations.AlterField(
            model_name='uevent4',
            name='line2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='uevent4',
            name='line3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
