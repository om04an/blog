from django.urls import path

from . import views

urlpatterns = [
    path('<int:post_id>/', views.post),
    path('comment/', views.comment, name='add_comment'),
    ]