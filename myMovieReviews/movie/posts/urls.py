from django.urls import path
from . import views

app_name="posts"

urlpatterns=[
    path('',views.home,name="home"),
    path('create',views.create,name="create"),
    path('posts/<int:pk>',views.retrieve,name="retrieve"),
    path('posts/<int:pk>/update',views.update,name="update"),
]