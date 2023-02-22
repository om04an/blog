# Generated by Django 4.1.7 on 2023-02-22 02:22

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='static/images/avatar/main.jpg', force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='static/images/avatar'),
        ),
    ]
