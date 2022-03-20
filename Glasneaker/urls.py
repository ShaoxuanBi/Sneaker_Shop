# Glasneaker 的子路由

from django.urls import path
from Glasneaker import views

urlpatterns = [
    path('', views.index, name='index'),  # url地址对应程序，主页
    path('login/', views.login, name='login'),
    path('check_login/', views.check_login, name='check_login'),
    path('register/', views.register, name='register'),
    path('check_register/', views.check_register, name='check_register'),
    path('logout/', views.logout, name='logout'),
    path('airjordan/', views.airjordan, name='airjordan'),
    path('yeezy/', views.yeezy, name='yeezy'),
    path('product/<str:id>', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('finished/', views.finished, name='finished'),
    path('cart/', views.cart, name='cart'),
    path('nike/', views.nike, name='nike'),
    path('adidas/', views.adidas, name='adidas'),
    path('secondary/', views.secondary, name='secondary'),

    # path('cartadd',views.cart_add, name='cart_add'),
    # path('cartremove',views.cart_remove, name='cart_remove'),

]
