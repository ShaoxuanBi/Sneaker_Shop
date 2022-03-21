# 呈现给用户界面的相应
from unicodedata import name
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Brand, Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    return render(request, 'Glasneaker/register.html')


def check_register(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    fisrtname = request.POST.get('fisrtname', None)
    lastname = request.POST.get('lastname', None)
    if username and password:
        new_user = User.objects.create()
        new_user.username = username
        new_user.password = password
        new_user.email = email
        new_user.fisrtname = fisrtname
        new_user.lastname = lastname
        new_user.save()
        print("注册成功")
        return redirect('/login/')
    else:
        return HttpResponse("注册失败,用户名和密码不能为空")


def login(request):
    return render(request, 'Glasneaker/login.html')


def check_login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = User.objects.get(username=username)
    if user.password == password:
        print("登录成功")
        request.session['user_id'] = user.id
        request.session['user_name'] = user.username
        request.session['cart'] = []
        request.session['totalprice'] = 0
        return redirect('/')
    else:
        return HttpResponse("登录失败")
        # return redirect('/login/')


def logout(request):
    request.session.flush()
    return redirect("/")


def index(request):
    brand = Brand.objects.get(name="airjordan")
    prod = Product.objects.filter(brand=brand)[:6]
    data1 = []
    for item in prod:
        i = {}
        i['id'] = item.id
        i['name'] = item.productname
        i['picture'] = '''<img src='/static/images/%s'>''' % item.picture
        i['price'] = item.price
        data1.append(i)
    brand = Brand.objects.get(name="yeezy")
    prod = Product.objects.filter(brand=brand)[:6]
    data2 = []
    for item in prod:
        i = {}
        i['id'] = item.id
        i['name'] = item.productname
        i['picture'] = '''<img src='/static/images/%s'>''' % item.picture
        i['price'] = item.price
        data2.append(i)
    return render(request, "Glasneaker/index.html", {"data1": data1, "data2": data2})


def airjordan(request):
    brand = Brand.objects.get(name="airjordan")
    prod = Product.objects.filter(brand=brand)
    data = []
    for item in prod:
        i = {}
        i['id'] = item.id
        i['name'] = item.productname
        i['picture'] = '''<img src='/static/images/%s'>''' % item.picture
        i['price'] = item.price
        data.append(i)
    # print(data)
    return render(request, "Glasneaker/AJ.html", {"data": data})


def yeezy(request):
    brand = Brand.objects.get(name="yeezy")
    prod = Product.objects.filter(brand=brand)

    data = []
    for item in prod:
        i = {}
        i['id'] = item.id
        i['name'] = item.productname
        i['picture'] = '''<img src='/static/images/%s'>''' % item.picture
        i['price'] = item.price
        data.append(i)
    # print(data)
    return render(request, "Glasneaker/yeezy.html", {"data": data})


def nike(request):
    brand = Brand.objects.get(name="airjordan")
    prod = Product.objects.filter(brand=brand)
    data = []
    for item in prod:
        i = {}
        i['id'] = item.id
        i['name'] = item.productname
        i['picture'] = '''<img src='/static/images/%s'>''' % item.picture
        i['price'] = item.price
        data.append(i)
    return render(request, "Glasneaker/Nike.html", {"data": data})


def adidas(request):
    brand = Brand.objects.get(name="yeezy")
    prod = Product.objects.filter(brand=brand)

    data = []
    for item in prod:
        i = {}
        i['id'] = item.id
        i['name'] = item.productname
        i['picture'] = '''<img src='/static/images/%s'>''' % item.picture
        i['price'] = item.price
        data.append(i)
    # print(data)
    return render(request, "Glasneaker/Adidas.html", {"data": data})


def order(request):
    return render(request, "Glasneaker/order.html")


def finished(request):
    request.session['cart'] = []
    request.session['totalprice'] = 0
    return render(request, "Glasneaker/finished.html")


def product(request, id):
    prod = Product.objects.get(id=id)
    item = {}
    item['id'] = prod.id
    item['brand'] = prod.brand
    item['name'] = prod.productname
    item['description'] = prod.description
    item['picture'] = '''<a href="/static/images/%s" class="jqroom"><img src="/static/images/%s" ></a>''' % (
        prod.picture, prod.picture)
    item['price'] = prod.price
    item['quantity'] = prod.quantity
    return render(request, 'Glasneaker/product.html', item)


def cart(request):
    if request.method == "POST":
        id = request.POST.get('id')
        radio = request.POST.get('customRadioInline1', None)
        number = request.POST.get('number')
        prod = Product.objects.get(id=id)
        price = float(prod.price)
        item = {}
        item['id'] = id
        item['price'] = price
        item['prices'] = int(number)*price
        item['number'] = number
        item['size'] = radio
        item['name'] = prod.productname
        item['picture'] = '''<img src='/static/images/%s'>''' % prod.picture
        request.session['cart'].append(item)
        request.session['totalprice'] += item['prices']
    return render(request, "Glasneaker/cart.html")


def cart_remove(request):
    id = request.POST.get('id')
    return render(request, "Glasneaker/cart.html")


def comment(request):
    return render(request, "Glasneaker/comment.html")


def secondary(request):
    return render(request, "Glasneaker/secondary.html")
