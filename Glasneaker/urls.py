# Glasneaker 的子路由

from django.urls import path
from Glasneaker import views

urlpatterns = [
    path('', views.index, name='index'), # url地址对应程序，主页
]