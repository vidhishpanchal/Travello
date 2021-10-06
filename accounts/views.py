from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Inavlid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email already exists...")
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                messages.info(request, "User Created successfully.")
                return redirect('login')
        else:
            print("password not matching...")
            messages.info(request, "Passwords not matching...")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
