from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart',views.cart,name="cart")
    # using this path('about') we can go to /about route to view the template
]
