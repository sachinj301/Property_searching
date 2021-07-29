from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username is already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email address is already in use.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password,
                                                    email=email, first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    messages.success(request, "Your successfully registered and Now can Log-In")
                    return redirect('login')
        else:
            messages.error(request, "Password Do not match.")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now Logged Out.")
        return redirect('index')
