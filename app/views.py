from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def First(request):
    return HttpResponse('<h1>This is First page</h1>')

def Second(request):
    return HttpResponse('<h1>This is Second page</h1>')