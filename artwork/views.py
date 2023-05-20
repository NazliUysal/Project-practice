from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.template import loader


# Create your views here.

def home(request):
    return render (request, "index.html")

@login_required(login_url="home")
def timeline(request):
    posts = Post.objects.all()
    user = request.user
    return render (request, "artwork/timeline.html", {'user':user, 'posts':posts})

@login_required
def upload(request):
    return render (request, "artwork/upload.html")


@login_required
def postDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render (request, "artwork/artwork.html", {'post':post})


# @login_required
# def timeline(request):
#     user = request.user #get logged in user
#     posts = Stream.objects.filter(user=user) #filters and gets posts of the logged in user
    
#     group_ids = []

#     for post in posts:
#         group_ids.append(post.post_id)
#     post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
#     context = {
#         'post_items': post_items
#     }
#     return render(request, 'accounts/timeline.html', context)

