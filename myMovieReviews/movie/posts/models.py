from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50) #제목
    year=models.IntegerField() #개봉년도
    genre=models.CharField(max_length=50) #장르
    star=models.FloatField() #별점
    director=models.CharField(max_length=50) #감독
    actor=models.CharField(max_length=50)
    runtime=models.IntegerField()
    review=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)