from django.urls import path
from . import views

app_name = 'stagram'

urlpatterns = [
    path('', views.home, name='home'),
    path('comment_del', views.comment_del, name='comment_del'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
]