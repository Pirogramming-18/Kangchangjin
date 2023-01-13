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

def retrieve(request:HttpRequest,pk,*args,**kwargs):
    post=Post.objects.all().get(pk=pk)
    return render(request,"posts/retrieve.html",{'post':post})

def update(request: HttpRequest,pk,*args,**kwargs):
    post=Post.objects.get(pk=pk)

    if request.method=="POST":
        post.title=request.POST["title"]
        post.year=request.POST["year"]
        post.genre=request.POST["genre"]
        post.star=request.POST["star"]
        post.runtime=request.POST["runtime"]
        post.review=request.POST["review"]
        post.director=request.POST["director"]
        post.actor=request.POST["actor"]   
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request,"posts/update.html",{"post":post})