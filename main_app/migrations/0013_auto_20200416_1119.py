# Generated by Django 3.0.3 on 2020-04-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200416_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='feeling',
            field=models.CharField(choices=[('choice1', 'U+1F600'), ('choice2', 'https://imgur.com/71F3z7x.jpeg'), ('choice3', 'https://imgur.com/5C0AHib.jpeg'), ('choice4', 'https://imgur.com/iASVG4S.jpeg')], max_length=100, verbose_name='How do you feel today ?'),
        ),
    ]
