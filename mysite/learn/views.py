#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    string = u"hello,i'm neo!"
    TutorialList = ['HTML', 'CSS', 'JQuery', 'Python', 'Django']
    info_dict = {'site':u'hello', 'content':u'bye' }
    List = map(str, range(100))
    return render(request, 'learn/home.html', {'List':List})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request, 'home.html')

