from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User

# Register
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password = password)  # Xác thực user
            login(request, user)
            messages.success(request, ('Đăng ký thành công !'))
            return redirect('home')
        else:
            # Nếu form không hợp lệ, hiển thị lỗi
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/register.html', {'form' : form})

# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)  # Xác thực user
        if user is not None: # nếu tồn tại
            login(request, user) # cho đăng nhập
            messages.success(request,('đăng nhập thành công'))
            return redirect('home')
        else:
            messages.success(request, ('Sai tài khoản, mật khẩu hoặc tài khoản không tồn tại'))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')
    
#  logout 
def logout_user(request): # Đăng xuất user
    logout(request)   #  logout là thư viện đã import 
    messages.success(request, ("logout thành công "))
    return redirect('home') 



