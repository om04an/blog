from django.shortcuts import render
from .models import User, Profile


def home(request):
    data_user = ''
    if request.user.is_authenticated:
        user = request.user
        data_user = Profile.objects.get(user=user)
    
    return render(request, 'index.html', {'data_user': data_user})
