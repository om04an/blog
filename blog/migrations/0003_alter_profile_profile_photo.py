# Generated by Django 4.1.7 on 2023-02-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_profile_last_visit_remove_profile_nickname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(upload_to='static/images/avatar'),
        ),
    ]
