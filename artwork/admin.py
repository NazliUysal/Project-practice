from django.contrib import admin

# Register your models here.

from artwork.models import Profile, Post
admin.site.register(Profile)
admin.site.register(Post)
