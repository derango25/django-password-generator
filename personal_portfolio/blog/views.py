from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
