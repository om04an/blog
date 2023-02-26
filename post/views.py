from django.shortcuts import render, redirect
from blog.models import User, Profile, Post, Comment


# Create your views here.
def post(request, post_id):
    data_user = ''
    if request.user.is_authenticated:       # checking if the user is authorized
        data_user = _getting_user_data(request)

    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    users = User.objects.all()
    

    return render(request, 'post.html', {'post':post,
                                         'data_user': data_user,
                                         'comments': comments,
                                         'users': users,
                                         })


def _getting_user_data(request):
    nickname = request.user     # obtaining a nickname of an authorized user
    
    if not Profile.objects.filter(user=nickname):   # check there is an entry in the profile table and if not, then a default entry is added
        user = Profile(user=nickname, number_of_posts=0)
        user.save()

    data_user = Profile.objects.get(user=nickname)

    return data_user
