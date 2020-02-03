from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
# Create your views here.


def index(request):
    return render(request, 'home.html')


def individual_post(request):
    return HttpResponse('Hi, I have no Idea what I am doing. Maybe a post will be here someday.')


def posts(request):
    return render(request, 'post.html')
