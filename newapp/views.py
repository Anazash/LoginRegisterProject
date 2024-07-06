from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserProfile

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Create the user
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.save()

        # Create UserProfile
        user_profile = UserProfile(user=user, gender=gender)
        user_profile.save()

        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')
