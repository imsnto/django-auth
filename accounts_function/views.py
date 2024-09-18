from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts_function/register.html', {'form': form})

@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts_function/login.html', {'form': form})

@never_cache
@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')

@never_cache
@login_required(login_url='login')
def home(request):
    return render(request, 'accounts_function/home.html')