from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm  # Fixed typo in the form import
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login  # Avoids conflict with built-in login
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Fixed form name
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()  # Fixed form name
    return render(request, 'users/register.html', {'form': form})


def user_login(request):  # Renamed function to avoid conflicts
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Using Django's built-in login function
                messages.success(request, f"Welcome back, {username}!")
                return redirect("home")  # Redirect to home or dashboard
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})
