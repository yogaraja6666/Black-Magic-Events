# Generated by Django 4.2 on 2023-04-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_levent1_title_levent1_line1_levent1_line2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levent1',
            name='line1',
            field=models.TextField(default='ytj', max_length=19),
        ),
    ]