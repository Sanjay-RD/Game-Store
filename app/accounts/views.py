from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def account(request):
    return render(request,'accounts/account.html')

def login(request):
    if request.method == "POST":
        print('login')
        messages.error(request,'Testing error message')
        return redirect('account')


def register(request):
    if request.method == "POST":
        print('register')
        messages.error(request, 'Testing error message')
        return redirect('account')


def logout(request):
    return redirect('index')
