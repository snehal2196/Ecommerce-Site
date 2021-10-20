from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index(request):
    posts = Blogpost.objects.all()
    params = {'posts':posts}
    return render(request, 'blog/index.html',params)

def blogpost(request, id):
    posts = Blogpost.objects.filter(post_id=id)[0]
    print(posts)
    params = {'postContent':posts}
    return render(request, 'blog/blogpost.html', params)