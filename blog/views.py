from django.shortcuts import render, redirect
from .models import User, Profile, Post, Comment


def home(request):
    data_user = ''
    if request.user.is_authenticated:       # checking if the user is authorized
        data_user = _getting_user_data(request)

    posts = post_search(request)    
    comments = Comment.objects.all()

    _updating_post_and_user_data()

    render_page = render(request, 'index.html', {'data_user': data_user,
                                          'posts': posts,
                                          'comments': comments,
                                          })

    return render_page

def _updating_post_and_user_data():
    _update_the_number_of_likes_and_user_posts()
    _update_post_comment_count()


def post_search(request):
    query_dict = request.GET    # This is a dict
    query = query_dict.get('post')      # user request

    if query:
        if Post.objects.filter(title__contains=query):      
            posts = Post.objects.filter(title__contains=query)      # title search
        else:
            posts = Post.objects.filter(text__contains=query)       # search by post text
    else:
        posts = Post.objects.all()
    return posts


def _getting_user_data(request):
    nickname = request.user     # obtaining a nickname of an authorized user

    if not Profile.objects.filter(user=nickname):   # check there is an entry in the profile table and if not, then a default entry is added
        user = Profile(user=nickname, number_of_posts=0)
        user.save()

    data_user = Profile.objects.get(user=nickname)

    return data_user


def _update_the_number_of_likes_and_user_posts():
    users = Profile.objects.all()

    for user in users:      # update the number of posts and comments for each user
        user.number_of_posts = len(Post.objects.filter(user_id=user.id))
        user.number_of_comments = len(Comment.objects.filter(commenter_id=user.id))
        user.save()


def _update_post_comment_count():
    posts = Post.objects.all()

    for post in posts:      # update the number of comments for each post
        post.number_of_comments = len(Comment.objects.filter(post_id=post.id))
        post.save()