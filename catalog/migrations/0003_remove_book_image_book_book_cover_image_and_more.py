# Generated by Django 4.0.2 on 2022-02-18 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_customuser_is_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='book_cover_image',
            field=models.ImageField(blank=True, default='default-profile.jpeg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-profile.jpeg', null=True, upload_to=''),
        ),
    ]
