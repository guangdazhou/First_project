
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from App.models import Wheel, Showgoods, User


def index(request):# 首页
    wheels = Wheel.objects.all()

    username = request.session.get('username')

    data = {
        'wheels':wheels,
        'username': username
    }

    return render(request,'Homepage.html',context=data)


def register(request): # 注册
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

def login(request):  # 登录
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

def logout(request): # 退出
    response = redirect('app:Homepage')
    del request.session['username']

    return response


def Men(request): # 商品部分展示，点击图片获取详细信息
    showgoods = Showgoods.objects.all()
    return render(request,'Men.html',context={"showgoods":showgoods})


def GoodsDetails(request,goodsid): # 商品详细信息展示页面
    showgoods = Showgoods.objects.filter(goodsid=goodsid)


    data = {
        'showgoods':showgoods
    }

    return render(request,'GoodsDetails.html',context=data)


def shoppingbag(request): # 没完成 购物袋
    return render(request,'shoppingbag.html')

# def index(request):
#     wheels = Wheel.objects.all()
#
#     username = request.session.get('username')
#
#     data = {
#         'wheels':wheels,
#         'username': username
#     }
#
#     return render(request,'Homepage.html',context=data)


# def showgoods(request,goodsid): # 点击得到的商品详情页面，自己创建的
#
#     showgoods = Showgoods.objects.filter(goodsid=goodsid)
#
#
#     data = {
#         'showgoods':showgoods
#     }
#
#     return render(request,'showgoods.html',context=data)