from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

# Create your models here.
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=30)
    food_name=models.CharField(max_length=30)
    place=models.CharField(max_length=50)
    cost=models.IntegerField()
    rating = models.IntegerField()
    img = models.ImageField(blank=True, null=True,upload_to='media/')
    restaurant_img = models.ImageField(blank=True, null=True,upload_to='media/')


    def __str__(self):
        return self.restaurant_name
    
class Signup(models.Model):
    Rid= models.CharField(max_length=50)
    Rpswd= models.CharField(max_length=35)

    #Aid='username'
    #Apswd='password'
    def __str__(self):
        return self.Rid

class Branch(models.Model):
    pass

