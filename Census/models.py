from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Blogs(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=500)
    img=models.ImageField(upload_to='images/')
    time=models.DateTimeField(auto_now_add=True)
    link=models.CharField(max_length=200)
    


    