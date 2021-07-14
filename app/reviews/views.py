from django.shortcuts import redirect, render
from .models import Review
from django.contrib import messages

# Create your views here.


def createReview(request, blog_id):
    blog_id = request.POST['blog_id']
    user_id = request.POST['user_id']
    user_name = request.POST['user_name']
    rating = request.POST['rating']
    comments = request.POST['comments']
    if request.method == "POST":
        # print(blog_id,user_id,user_name,rating,comments)

        if request.user.is_authenticated:
            # user_id = request.user.id
            has_connected = Review.objects.all().filter(blog_id=blog_id)
            if has_connected:
                messages.error(request,'You Have Already Posted a Review')
                return redirect('/blogs/'+blog_id)

        review = Review(blog_id=blog_id,user_id=user_id,user_name=user_name,rating=rating,comments=comments)
        review.save()
        return redirect('/blogs/'+blog_id)
