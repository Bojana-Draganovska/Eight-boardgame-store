from django.shortcuts import render, redirect
from .models import Category, Game, Order, Customer, Toy
from .forms import CustomerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#home page

def index(request):
    games_home = Game.objects.all
    fave_game = Game.objects.first()
    all_categories = Category.objects.all()
    return render(request, "home.html", {'games': games_home, 'fave': fave_game, 'request': request, 'all_categories': all_categories})

def details(request, id):
    game = Game.objects.get(id = id)
    return render(request, "details.html", {'game': game})

def toys(request):
    toys = Toy.objects.all
    all_categories = Category.objects.all()
    return render(request, "toys.html", {'toys': toys, 'all_categories': all_categories})

def detailstoys(request, id):
    toy = Toy.objects.get(id = id)
    return render(request, "detailstoys.html", {'toy': toy})


@login_required(login_url='/login')
def payment(request):
    return render(request, "payment.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=CustomerForm()
        
        if request.method == "POST":
            
            form=CustomerForm(request.POST)
            # print(form)
            print(form.errors)
            if form.is_valid():
                print('here')
                userobj = form.save()
                user = form.cleaned_data.get('username')
                customer = Customer.objects.create(user= userobj)
                customer.save()
                return redirect('/login')        
            
    return render(request, "signup.html")

def categories(request):
    all_games = Game.objects.all
    all_categories = Category.objects.all
    return render(request, 'categories.html', {'allgames': all_games, 'all_categories': all_categories})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            print(username)
            print(password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, "login.html", {})

        return render(request, "login.html")
    
def logoutUser(request):
    logout(request)
    return redirect('/login')

def profile(request):
    return render(request, "profile.html")

def administrator(request):
    return render(request, "administrator.html")

def categoryFilter(request, categoryId):
    categories = Category.objects.all()
    selected_category = Category.objects.get(id = categoryId)

    gamesByCat = Game.objects.all().filter(category = selected_category)
   

    return render(request, "categories.html", {'allgames': gamesByCat})