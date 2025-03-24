from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from members.models import UserProfile
from members.forms import *


def register(request):
    if request.user.is_authenticated:
        return redirect("home")  
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
# Lưu user trước
            use = form.save()
# Tạo UserProfile
            UserProfile.objects.create(
                user = use,
                phoneNumber = form.cleaned_data['phoneNumber'],
                # avatar = form.cleaned_data['avatar']
                )
# Xác thực user sau khi đăng ký
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password = password)  # Xác thực user
            
            if user is not None:
                login(request, user)
                messages.success(request, "Đăng ký thành công!")
                return redirect("home")
            else:
                messages.error(request, "Lỗi xác thực! Vui lòng thử lại.")
        else:
            # Nếu form không hợp lệ, hiển thị lỗi
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form' : form})