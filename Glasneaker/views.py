
# 呈现给用户界面的相应

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Glasneaker/index.html");

def login(request):
    return render(request, "Glasneaker/login.html");

def register(request):
    return render(request, "Glasneaker/register.html");
