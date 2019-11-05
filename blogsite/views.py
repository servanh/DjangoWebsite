from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello, welcome to the home page.')


def individual_post(request):
    return HttpResponse('Hi, I have no Idea what I am doing. Maybe a post will be here someday.')


