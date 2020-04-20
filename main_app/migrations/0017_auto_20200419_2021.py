# Generated by Django 3.0.5 on 2020-04-20 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20200417_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='partner',
        ),
        migrations.AddField(
            model_name='partner',
            name='description',
            field=models.CharField(default='friend', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='entry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Entry'),
            preserve_default=False,
        ),
    ]
