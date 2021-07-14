from django.urls import path
from . import views

urlpatterns=[
    path('<int:blog_id>/',views.createReview,name="createReview")
]