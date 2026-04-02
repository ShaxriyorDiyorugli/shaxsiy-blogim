from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):
    context = {
        'title': 'Shaxriyor\'s Blog',
    }
    return render(request, 'app/index.html', context)

def blog(request):
    return render(request, 'app/blog.html', {})

def about(request):
    return render(request, 'app/about.html', {})