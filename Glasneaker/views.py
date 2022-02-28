
# 呈现给用户界面的相应

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect    # 页面跳转重定向

def index(request):
    return render(request,"Glasneaker/index.html");

