from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:10]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})

def blog_archive(request):
    blog_archive = Blog.objects.order_by('-date')
    return render(request, 'blog/blog_archive.html', {'blog_archive':blog_archive})