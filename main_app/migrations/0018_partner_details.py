# Generated by Django 3.0.5 on 2020-04-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_partner_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='details',
            field=models.CharField(default='friend', max_length=50),
            preserve_default=False,
        ),
    ]
