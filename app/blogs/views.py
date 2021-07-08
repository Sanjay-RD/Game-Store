from django.shortcuts import render

# Create your views here.


def blog(request, blog_id):
    return render(request, 'blogs/blog.html')


def blogs(request):
    return render(request, 'blogs/blogs.html')
