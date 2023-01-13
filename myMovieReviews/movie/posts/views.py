from django.shortcuts import render,redirect
from .models import Post
from django.http.request import HttpRequest
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request, "posts/home.html",{"posts":posts})

def create(request:HttpRequest,*args,**kwargs):
    if request.method=="POST":
        print(request.POST)
        Post.objects.create(
            title=request.POST["title"],
            year=request.POST["year"],
            actor=request.POST["actor"],
            genre=request.POST["genre"],
            star=request.POST["star"],
            director=request.POST["director"],         
            runtime=request.POST["runtime"],
            review=request.POST["review"],        
        )
        return redirect("/")
    return render(request,"posts/create.html")