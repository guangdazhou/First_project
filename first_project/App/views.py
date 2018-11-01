from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from App.models import Wheel


def index(request):
    # wheels = Wheel.objects.all()

    username = request.session.get('username')

    data = {
        # 'wheels':wheels,
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

        # 存入数据库
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
        # 验证
        password = request.POST.get('password')

        users = User.objects.filter(username=username, password=password)
        if users.exists():

            user = users.first()

            # 状态保持 - 设置cookie
            # 状态保持 - 设置session
            request.session['username'] = username
            request.session.set_expiry(180)


            return redirect('app:Homepage')
        else:
            return HttpResponse('用户名或密码错误')

def logout(request):
    response = redirect('app:Homepage')

    ## session
    # 方式一: session是借助于cookie
    # response.delete_cookie('sessionid')

    # 方式二: 直接删除session存储
    del request.session['username']

    # 方式三: 同时删除cookie和session
    # request.session.flush()



    return response