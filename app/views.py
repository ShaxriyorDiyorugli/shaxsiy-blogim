from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.filter(is_publish=True).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)
