from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:id>', views.details, name="details"),
    path('login', views.loginPage, name='loginPage'),
    path('signup', views.signup, name="signup"),
    path('categories', views.categories, name="categories"),
    path('toys', views.toys, name='toys'),
    path('detailstoys/<int:id>', views.detailstoys, name="detailstoys"),
    path('profile/', views.profile, name="profile"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('administrator', views.administrator, name="administrator"),
    path('categoryFilter/<int:categoryId>', views.categoryFilter, name="categoryFilter"),
    path('toyCategoryFilter/<int:toyCategoryId>', views.toyCategoryFilter, name="toyCategoryFilter"),
    path('newgame', views.newgame, name="newgame"),
    path('newtoy', views.newtoy, name="newtoy"),
    path('basket/<int:id>', views.basket, name="basket"),
    path('basketToy/<int:id>', views.basketToy, name="basketToy"),
    path('payment/<str:item_type>/<int:id>', views.payment, name='payment'),
    path('orderSuccess', views.orderSuccess, name="orderSuccess"),
    path('add_game_item', views.add_game_item, name='add_game_item'),
    path('add_toy_item', views.add_toy_item, name='add_toy_item'),
]


