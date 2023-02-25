from django.shortcuts import render
from .models import User, Profile, Post, Comment


def home(request):
    data_user = ''
    if request.user.is_authenticated:
        data_user = _getting_user_data(request)
    posts = Post.objects.all()
    comments = Comment.objects.all()
    update_users()

    return render(request, 'index.html', {'data_user': data_user,
                                          'posts': posts,
                                          'comments': comments,
                                          })


def _getting_user_data(request):
    nickname = request.user     # obtaining a nickname of an authorized user

    if not Profile.objects.filter(user=nickname):   # check there is an entry in the profile table and if not, then a default entry is added
        user = Profile(user=nickname, number_of_posts=0)
        user.save()

    data_user = Profile.objects.get(user=nickname)

    return data_user


def update_users():
    users = Profile.objects.all()

    for user in users:
        user.number_of_posts = len(Post.objects.filter(user_id=user.id))
        user.number_of_comments = len(Comment.objects.filter(commenter_id=user.id))
        user.save()