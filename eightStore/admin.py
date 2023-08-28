from django.contrib import admin
from .models import Category, Game, Customer, Order, Product, Toy, ToyCategory

# Register your models here.

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Toy)
admin.site.register(ToyCategory)