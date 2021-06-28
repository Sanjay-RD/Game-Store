from django.shortcuts import render

# views is use to render .html template

# index is function that we pass from urls ie-> views.index


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def account(request):
    return render(request,'pages/account.html')
