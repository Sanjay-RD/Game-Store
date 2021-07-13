from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>', views.blog, name="blog"),
    path('createBlog', views.createBlog, name="createBlog"),
    path('create',views.create,name="create"),
    path('editBlog/<int:blog_id>/',views.editBlog,name="editBlog"),
    path('deleteBlog/<int:blog_id>/',views.deleteBlog,name="deleteBlog")
]
