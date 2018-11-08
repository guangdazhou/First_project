from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from App.models import Wheel


def index(request):
    wheels = Wheel.objects.all()

    username = request.session.get('username')

    data = {
        'wheels':wheels,
        'username': username
    }

    return render(request,'Homepage.html',context=data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        RPwd = request.POST.get('RPwd')
        try:
            user = User()
            user.username = username
            user.password = password
            user.RPwd = RPwd
            user.save()

            request.session['username'] = username
            request.session.set_expiry(180)


            return redirect('app:Homepage')

        except Exception as e:
            return HttpResponse('注册失败' + e)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username, password=password)
        if users.exists():

            user = users.first()
            request.session['username'] = username
            request.session.set_expiry(180)
            return redirect('app:Homepage')
        else:
            return HttpResponse('用户名或密码错误')

def logout(request):
    response = redirect('app:Homepage')
    del request.session['username']

    return response


def Men(request):
    return render(request,'Men.html')


def GoodsDetails(request):
    return render(request,'GoodsDetails.html')


def shoppingbag(request):
    return render(request,'shoppingbag.html')