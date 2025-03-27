from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def auth_view(request):
    if request.method == 'POST':
        # Check if it's a sign-in or sign-up form based on the button value
        if 'login' in request.POST:
            # Handle login
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Muvaffaqiyatli kirdingiz!")
                return redirect('home')  # Redirect to a home page
            else:
                messages.error(request, "Foydalanuvchi nomi yoki parol noto‘g‘ri.")

        elif 'signup' in request.POST:
            # Handle sign-up
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Bu foydalanuvchi nomi allaqachon mavjud.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Bu email allaqachon ro‘yxatdan o‘tgan.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                messages.success(request, "Muvaffaqiyatli ro‘yxatdan o‘tdingiz!")
                return redirect('home')  # Redirect to a home page

    # Render the form page for GET requests or failed POST attempts
    return render(request, 'signing.html')