from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FoodType(models.Model):
    name = models.CharField(max_length=50)

class Food(models.Model):
    food_type = models.ForeignKey(FoodType,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    tarkibi = models.ManyToManyField('Tarkibi')
    price = models.DecimalField(max_digits=5,decimal_places=2)


class Tarkibi(models.Model):
    lavash_tarkib = models.TextField()
    burger_tarkib = models.TextField()
    kfc_tarkib = models.TextField()
    pitsa_tarkib = models.TextField()
    hotdog_tarkib = models.TextField()
    hotdog_tarkib = models.TextField()
    umumiy_tarkib = models.TextField()

class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
