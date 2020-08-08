from django.db import models

# Create your models here.
class Student(models.Model):
    
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    img = models.ImageField(upload_to='pics')
    password = models.CharField(max_length=40)
    eno = models.CharField(max_length=13)


    