from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Shayan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '24 May 2019'
    },
    {
        'author': 'Shayan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '25 May 2019'
    },
]


def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})
