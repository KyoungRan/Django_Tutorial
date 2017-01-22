from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Awesome job guys! This is the index page, of our polls application')
