from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Game, Order, Customer, Toy
from django.contrib.auth.models import User

class CustomerForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'customerCountry', 'customerCity', 'cityPostCode', 'customerAdress', 'product', 'total_price']
