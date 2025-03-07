from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from .models import UserProfile
from .forms import *

# Register
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
# Lưu user trước
            use = form.save()
            use = form.save()
# Tạo UserProfile
            UserProfile.objects.create(
                user = use,
                phoneNumber = form.cleaned_data['phoneNumber'])
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
        return render(request, 'login.html')
    
#  logout 
def logout_user(request): # Đăng xuất user
    logout(request)   #  logout là thư viện đã import 
    messages.success(request, ("logout thành công "))
    return redirect('home') 

# profile
@login_required(login_url='login')
def user_profile(request): 
    me = request.user
    user_profile = UserProfile.objects.get( user = me)
    return render(request, 'user_profile.html',{'user_profile' : user_profile})







