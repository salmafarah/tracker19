# Generated by Django 3.0.5 on 2020-04-15 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_entry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='day',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='min',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='month',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='year',
        ),
    ]
