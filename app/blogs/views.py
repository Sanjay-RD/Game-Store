from django.shortcuts import redirect, render
from .models import Blog
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import BlogForm
# Create your views here.


def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blog.html', context)


def blogs(request):
    blogs = Blog.objects.order_by('-published_date')
    print(blogs)
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs.html', context)


def createBlog(request):
    form = BlogForm()
    context={
        'form':form
    }
    return render(request, 'blogs/createBlog.html',context)


def create(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        user_name=request.POST['user_name'] 
        blogTitle=request.POST['blogTitle'] 
        blogDescription = request.POST['blogDescription']
        blogImage=request.FILES['blogImage'] 
        # print(user_id,user_name,blogTitle,blogDescription,blogImage)
        blog = Blog(user_id=user_id,user_name=user_name,blogTitle=blogTitle,blogDescription=blogDescription,blogImage=blogImage)
        blog.save()
        messages.success(request,'Your Blogs has been created')

        # print(request.POST)

        # return redirect('blogs')
        return redirect('blogs')


def editBlog(request,blog_id):
    blogdata = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(instance=blogdata)

    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=blogdata)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request,'blogs/editBlog.html',context)


def deleteBlog(request,blog_id):
    blogdata = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blogdata.delete()
        messages.success(request,"Your Blog Has Been Deleted")
        return redirect('dashboard')
