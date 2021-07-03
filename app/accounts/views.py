from django.shortcuts import render,redirect

# Create your views here.

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def account(request):
    return render(request,'accounts/account.html')

def login(request):
    if request.method == "POST":
        print('login')
        return redirect('account')


def register(request):
    if request.method == "POST":
        print('register')
        return redirect('account')


def logout(request):
    return redirect('index')
