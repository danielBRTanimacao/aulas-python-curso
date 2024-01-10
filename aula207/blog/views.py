from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('blog')
    return HttpResponse('blog do app mais 1')

def exemplo(request):
    print('blog')
    return HttpResponse('exemplo do app mais 1')

def pidao(request):
    print('blog')
    return HttpResponse('pidao kk do app mais 1')