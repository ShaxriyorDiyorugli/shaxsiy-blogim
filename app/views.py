from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, ProjectCategory, Projects

def index(request):
    context = {'title': "Shaxriyor's Blog"}
    return render(request, 'app/index.html', context)

def about(request):
    return render(request, 'app/about.html', {})

def blog(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'app/blog.html', context)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category, is_publish=True).order_by('-created_at')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'app/category_detail.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_publish=True)
    post.views += 1
    post.save()

    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            Comment.objects.create(post=post, name=name, body=body)
            return redirect('post_detail', pk=pk)

    comments = post.comments.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'app/post_detail.html', context)

def projects_list(request):
    categories = ProjectCategory.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'app/projects.html', context)
def project_detail(request, pk):
    project = get_object_or_404(Projects, pk=pk, is_publish=True)
    project.views += 1
    project.save()

    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            Comment.objects.create(project=project, name=name, body=body)  # ← post= o'rniga project=
            return redirect('project_detail', pk=pk)

    comments = project.comments.all()
    context = {
        'projects': project,
        'comments': comments,
    }
    return render(request, 'app/project_detail.html', context)