# Generated by Django 4.1.7 on 2023-02-24 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='static/images/avatar/main.jpg', force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='static/images/avatar')),
                ('number_of_posts', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('date_create', models.DateField()),
                ('number_of_likes', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profile')),
            ],
        ),
    ]
