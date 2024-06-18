from django.shortcuts import redirect
from .models import BlogPost, Tags
from django.contrib import messages

def filter_by_name(request,name):
    object = None
    try:
        posts = BlogPost.objects.filter(title__icontains=name)
        object = posts
    except BlogPost.DoesNotExist:
        messages.error(request, "There is nothing with this title")
        return redirect("blog:blog_main")
    return object

