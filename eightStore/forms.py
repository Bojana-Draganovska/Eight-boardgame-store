from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Game, Customer, Toy
from django.contrib.auth.models import User

class CustomerForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']

class GameItemForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'short_description', 'long_description', 'price', 'playing_time', 'num_players', 'age', 'language', 'category', 'type'] 

class ToyItemForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['title', 'short_description', 'long_description', 'price', 'age', 'category', 'type'] 
