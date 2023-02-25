from django.contrib import admin
from .models import Profile, Post, Comment


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'number_of_posts', 'number_of_comments')
    fields = ('user', 'profile_photo', 'number_of_posts', 'number_of_comments')
    readonly_fields = ('number_of_posts', 'number_of_comments')


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_create', 'number_of_likes')
    fields = ('user', 'title', 'text', 'date_create', 'number_of_likes')
    readonly_fields = ('date_create', 'number_of_likes')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commenter', 'text', 'date_create')
    fields = ('post', 'commenter', 'text', 'date_create')
    readonly_fields = ('date_create',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)