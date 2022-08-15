from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm
from django.contrib import messages

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'app/register.html', context)

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or password is incorrect.')
    context = {'form': form}
    return render(request, 'app/login.html', context)

def homepage(request):
    return render(request, 'app/homepage.html')