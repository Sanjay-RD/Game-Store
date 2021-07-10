from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>', views.blog, name="blog"),
    path('createBlog', views.createBlog, name="createBlog"),
    path('create',views.create,name="create")
]
