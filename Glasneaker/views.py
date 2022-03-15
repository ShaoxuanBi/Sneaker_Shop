
# 呈现给用户界面的相应

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Glasneaker/index.html")

def login(request):
    return render(request, "Glasneaker/login.html")

def register(request):
    return render(request, "Glasneaker/register.html")

def airjordan(request):
    return render(request, "Glasneaker/AJ.html")

def yeezy(request):
    return render(request, "Glasneaker/yeezy.html")

def detail(request):
    return render(request, "Glasneaker/detail.html")

def order(request):
    return render(request, "Glasneaker/order.html")

def finished(request):
    return render(request, "Glasneaker/finished.html")

def cart(request):
    return render(request, "Glasneaker/cart.html")