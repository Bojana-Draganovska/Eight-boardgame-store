from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class ToyCategory(models.Model):
    name=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name    
    
class Game(models.Model):
    title=models.CharField(max_length=200, null=True)
    short_description=models.TextField(max_length=300, null=True)
    num_players=models.IntegerField()
    playing_time=models.IntegerField()
    age=models.IntegerField()
    language=models.CharField(max_length=200, null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    long_description=models.TextField(max_length=1000, null=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='static/games', null=True)
    type=models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title

class Toy(models.Model):
    title=models.CharField(max_length=200, null=True)
    short_description=models.TextField(max_length=300, null=True)
    age=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    long_description=models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='static/toys', null=True)
    category=models.ForeignKey(ToyCategory, on_delete=models.SET_NULL, null=True, default='boardgame.jpg')
    type=models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.title

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class Product(models.Model):

    game=models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    quantity=models.PositiveIntegerField()




