from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def register(request):

    return render(request,'regsiter.html')


def login(request):
    return render(request,'login.html')


def shoppingbag(request):
    return render(request,'shoppingbag.html')