# Glasneaker 的子路由

from django.urls import path
from Glasneaker import views

urlpatterns = [
    path('', views.index, name='index'), # url地址对应程序，主页
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('shopcar.jsp/',views.basket, name='basket'),
    path('index/product/',views.product, name='product'),
    path('index/basket/',views.basket, name='basket'),
    path('index/basket/',views.basket_add, name='basket_add'),
    path('index/basket/',views.basket_remove, name='basket_remove'),
]