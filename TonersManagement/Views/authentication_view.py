from django.shortcuts import render , redirect
from django.http import HttpResponse
from ..models import *
from django.contrib.auth.forms import UserCreationForm 
from ..forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request): 
    form = CreateUserForm()
    if request.method == "POST" :
        getten_form = CreateUserForm(request.POST)
        if getten_form.is_valid: 
            getten_form.save()

    return render(request,'TonersManagement/pages/register.html', {'form': form})


def loginpage(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('toners')
        else:
            messages.error(request,"Please enter a valid username and passsword", extra_tags="danger")
            return redirect('/login')

    return render(request,'TonersManagement/pages/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')