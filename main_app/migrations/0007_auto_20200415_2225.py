# Generated by Django 3.0.3 on 2020-04-16 03:25

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_entry_health'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='health',
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', multiselectfield.db.fields.MultiSelectField(choices=[('choice1', 'I have Covid'), ('choice2', 'I recovered from'), ('choice3', 'I have fell sick'), ('choice4', 'Im not sick')], max_length=31)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Entry')),
            ],
        ),
    ]