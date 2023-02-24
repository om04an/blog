from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='static/images/avatar', null=True, default='static/images/avatar/main.jpg')
    number_of_posts = models.IntegerField()

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + ' | ' + str(self.title)[:60] + '...'