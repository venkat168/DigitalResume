from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    school=models.CharField(max_length=500)
    diploma=models.CharField(max_length=500)
    degree=models.CharField(max_length=500)
    skill=models.TextField(max_length=200)
    about_you=models.TextField(max_length=300)

