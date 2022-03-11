# 呈现给用户界面的相应
from Glasneaker.models import User
from Glasneaker.models import Administrator
from Glasneaker.models import Product
from Glasneaker.models import Comment
from Glasneaker.models import Basket
from Glasneaker.models import Order
#from Glasneaker.models import OrderDetail
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Glasneaker/index.html");

def login(request):
    return render(request, "Glasneaker/login.html");

def register(request):
    return render(request, "Glasneaker/register.html");

def product(request):
    return render(request, "Glasneaker/product.html");

def basket(request):
    return render(request, "Glasneaker/basket.html");

def comment(request):
    return render(request, "Glasneaker/comment.html");

def order(request):
    return render(request, "Glasneaker/order.html");
