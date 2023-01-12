from django.shortcuts import render
from .models import Post
# from django.http.request import HttpRequest
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request, "posts/home.html",{"posts":posts})
