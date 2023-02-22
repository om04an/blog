from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_photo = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='static/images/avatar', null=True, default='static/images/avatar/main.jpg')
    number_of_posts = models.IntegerField()

    def __str__(self):
        return str(self.user)

