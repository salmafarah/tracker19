# Generated by Django 3.0.5 on 2020-04-16 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200416_0837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['-name']},
        ),
    ]