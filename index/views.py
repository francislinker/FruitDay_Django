from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        users = Users.objects.filter(uphone=uphone,upwd=upwd)
        if users:
            return HttpResponse('欢迎：'+users[0].uname)
        else:
            return HttpResponse('登录失败')

def cart(request):
    return render(request,"cart.html")

def register(request):
    if request.method == 'GET':
        return render(request,"register.html")
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']

        users = Users.objects.filter(uphone=uphone)
        if users:
            err = '电话号码已经存在'
            return render(request,'register.html',locals())

        Users.objects.create(uphone=uphone,upwd=upwd,uname=uname,uemail=uemail)
        return redirect('/')

