from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.login,name="login"),
    path("base/",views.base,name="base"),
    path("cart/",views.cart,name="cart"),
    path("register/",views.register,name="register"),
    path("checkout/",views.checkout,name="checkout"),
    path("home/",views.home,name="home"),
    
    # path("nhap/",views.nhap,name="nhap"),
     # path("menu/",views.menusign,name="menu"),
    
    
    
    
]
