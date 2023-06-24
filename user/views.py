from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def custom_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, "Bu username allaqachon foydalanilgan!")
            return redirect('register')
        if password1 != password2:
            messages.error(request, "Parollar mos kelmadi!")
            return redirect('register')
        user = User(
            username=username
        )
        user.set_password(password1)
        user.save()
        return redirect("login")
    return render(request, 'register.html')


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        messages.info(request, "Username yoki parol xato!")
        return redirect("login")
    return render(request, "login.html")
