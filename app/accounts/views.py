from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def account(request):
    return render(request,'accounts/account.html')

def login(request):
    if request.method == "POST":
        # get form value
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('account')
    else:
        return redirect('account')


def register(request):
    if request.method == "POST":
        #get form value
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm-password']
        # print(username,email,password,confirmPassword)
        #check if password match
        if password == confirmPassword:
            #check email
            if User.objects.filter(email=email).exists():
                messages.error(request,'This Email is already in use')
                return redirect('account')
            else:
                #looks good
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'You are now register and you can now login')
                return redirect('account')
        else:
            messages.error(request,'Password doesnot match')
            return redirect('account')
    else:
        return redirect('account')


def logout(request):
    return redirect('index')
