from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import registerForm
from .forms import loginForm


def register (request):
    form = registerForm()

    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "accounts/register.html", {'form':form})

def loginPage (request):
    if request.method == 'GET':
        form = loginForm()
        return render (request, "accounts/login.html", {'form':form})
    
    elif request.method == 'POST':
        form = loginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('timeline')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'accounts/login.html',{'form': form})
    


def logoutPage(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('home')

def timeline(request):
    return render (request, "accounts/timeline.html")

