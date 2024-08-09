from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
def login(request):
    context = {}
    return render(request,"app/login.html",context)
def base(request):
    context = {}
    return render(request,"app/base.html",context)
def cart(request):
    return render(request,"app/cart.html")
def checkout(request):
    return render(request,"app/checkout.html")
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
    context = {"form":form}
    return render(request , "app/register.html",context)
def home(request):
    context = {}
    return render(request , "app/home.html",context)
# def menusign(request):
#     context ={}
#     return render(request , "app/menusign.html",context)
# def nhap(request):
#     form  = UserCreationForm()
#     context = form
#     # if(request.method == "POST"):
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         form.save
        
#     # return render(request,"app/nhap.html",context)
