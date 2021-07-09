from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
# Create your views here.


def blog(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    context={
        'blog':blog
    }
    return render(request, 'blogs/blog.html', context)


def blogs(request):
    blogs = Blog.objects.order_by('-published_date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs.html', context)
