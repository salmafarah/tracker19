# Generated by Django 3.0.3 on 2020-04-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200415_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='health',
            field=models.CharField(choices=[('choice1', 'I have Covid'), ('choice2', 'I recovered from'), ('choice3', 'I have fell sick'), ('choice4', 'Im not sick')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Health',
        ),
    ]
