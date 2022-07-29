from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    pass

class Carousel(models.Model):
    first = models.CharField(max_length=100)    
    second = models.CharField(max_length=100) 
    nd = models.CharField(max_length=200)  
    narx = models.IntegerField()
    narx2 = models.IntegerField()
    images = models.ImageField()
    
    def __str__(self):
        return self.first
    
class Discover(models.Model):
    images = models.ImageField()
    names = models.CharField(max_length=50)
    malumot = models.CharField(max_length=150)
    def __str__(self):
        return self.names
 
