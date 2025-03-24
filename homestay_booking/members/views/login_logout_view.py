from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# login
def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")  

    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)  # Xác thực user
        if user is not None: # nếu tồn tại
            login(request, user) # cho đăng nhập
            messages.success(request,('đăng nhập thành công'))
            return redirect('home')
        else:
            messages.error(request, ('Sai tài khoản, mật khẩu hoặc tài khoản không tồn tại'))
            return redirect('login')
    else:
        return render(request, 'login.html')
    

# logout
def logout_user(request): # Đăng xuất user
    logout(request)   #  logout là thư viện đã import 
    messages.success(request, ("logout thành công "))
    return redirect('home') 