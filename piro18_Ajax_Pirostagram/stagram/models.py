from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    like = models.BooleanField(default=False)
    comment=models.CharField(max_length=100,blank=True,null=True)