# Generated by Django 3.0.5 on 2020-04-15 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200415_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
