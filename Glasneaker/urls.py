# Glasneaker 的子路由

from django.urls import path
from Glasneaker import views

urlpatterns = [
    path('', views.index, name='index'), # url地址对应程序，主页
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('airjordan/',views.airjordan, name='airjordan'),
    path('yeezy/',views.yeezy, name='yeezy'),
]