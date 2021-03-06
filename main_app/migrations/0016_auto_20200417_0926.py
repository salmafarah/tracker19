# Generated by Django 3.0.5 on 2020-04-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_merge_20200417_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='health',
            field=models.CharField(choices=[('choice1', 'I’ve been dignoised with COVID-19 and would like to create a record of my whereabouts'), ('choice2', 'I’ve recovered from COVID-19, but would like to track my whereabouts'), ('choice3', 'I’ve not been tested for COVID-19, but feel sick and want to track my whereabouts'), ('choice4', 'I do not have COVID-19 but would like to track my whereabout')], max_length=100, verbose_name='Which option best describes your health status'),
        ),
    ]
