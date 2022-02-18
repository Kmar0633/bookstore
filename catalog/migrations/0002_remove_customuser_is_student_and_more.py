# Generated by Django 4.0.2 on 2022-02-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_teacher',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mailing_address',
        ),
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(choices=[('e', 'kid customer'), ('a', 'adult customer'), ('b', 'admin')], default='e', help_text='Position Type', max_length=1),
        ),
    ]