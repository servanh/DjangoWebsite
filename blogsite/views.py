from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from .models import Post
from django.template import loader
from django.views import generic


# Create your views here.


# def index(request):
#     data = Post.objects.order_by('created_on')[:5]
#     template = loader.get_template('home.html')
#     context = {
#         'latest_posts_list': data,
#     }
#     return HttpResponse(template.render(context, request))


def individual_post(request):
    return HttpResponse('Hi, I have no Idea what I am doing. Maybe a post will be here someday.')


def posts(request):
    return render(request, 'post.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
