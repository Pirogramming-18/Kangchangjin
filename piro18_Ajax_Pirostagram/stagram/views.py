from django.shortcuts import render,redirect
from .models import Post
from django.http.request import HttpRequest

# Create your views here.
def home(request):
    post=Post.objects.all()
    
    return render(request,"stagram/home.html",{"post":post})


def comment_del(request:HttpRequest, pk, *args, **kwargs):
    if request.method=="POST":
        post=Post.objects.all()
        post.delete()
    return redirect("/")

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt #csrf보안설정을 해제시켜줌
def like_ajax(request):
    req=json.loads(request.body)
    likey=req['likey']

    if likey =='False':
        likey='True'
        return JsonResponse({'like': likey})
    else:
        likey = 'False'
        return JsonResponse({'like': likey})
