# 呈现给用户界面的相应
from django.conf import settings
from django.http import HttpResponse
from .models import User
from .models import Product
from .models import Promotion
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .forms import BasketAddProductForm

class Basket(object):

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:
            basket = self.session[settings.CART_SESSION_ID] = {}
        self.basket = basket
        self.promotionID = self.session.get('promotionID')

def register(request):
    return render(request, "Glasneaker/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('user', None)
        password = request.POST.get('password', None)
        message = "All fields must be filled in!"
        if username and password:
            username = username.strip()
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['user'] = user.name
                    return redirect('/')
                else:
                    message = "Incorrect password!"
            except:
                message = "Username does not exist!"
        return render(request, "Glasneaker/login.html", {"message": message})
    return render(request, "Glasneaker/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/index/")

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

def product(request):
    product = get_object_or_404(Product, id=id)
    basket_product_form = BasketAddProductForm()
    return render(request,'Glasneaker/product.html',{'product': product, 'basket_product_form': basket_product_form})

def basket(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = BasketAddProductForm(initial={'quantity': item['quantity']})
    return render(request, 'basket.html', {'basket': basket})
#   return render(request, "Glasneaker/basket.html");

def basket_add(request, productID):
    basket = Basket(request)
    product = get_object_or_404(Product, id=productID)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('Glasneaker:basket')

def basket_remove(request, productID):
    basket = Basket(request)
    product = get_object_or_404(Product, id=productID)
    basket.remove(product)
    return redirect('Glasneaker:basket')

def comment(request):
    return render(request, "Glasneaker/comment.html");

def order(request):
    return render(request, "Glasneaker/order.html");

