from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('home:index')
    else:
        form = RegisterForm()
    return render (request,'users/register.html',{'form':form})

def login_user(request):
    user = request.user

    if user.is_authenticated:
        logout(request)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                messages.info(request, 'Usernmae OR Password is wrong.')

    context = {

    }
    return render(request, 'users/login.html', context)

@login_required(login_url = 'users:login')
def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')