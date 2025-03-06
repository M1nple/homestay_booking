from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import*


#VIEWS
def home(request):
    homestays = Homestay.objects.all()
    return render(request, 'home.html', {'homestays': homestays})

@login_required(login_url='login')
def list_homestay(request):
    me = request.user
    homestays = Homestay.objects.filter(owner = me)
    return render(request, 'views/list_homestay.html',{'homestays': homestays})


#CREATE
@login_required(login_url='login')
def create_homestay(request):
    if request.method == "POST":
        form = FormHomestay(request.POST)
        if form.is_valid():
            homestay = form.save(commit=False)
            # homestay.owner = request.user.id
            homestay.owner = request.user
            homestay.save()
            messages.success(request,"them thanh cong")
            return redirect('home')
        else:
            messages.error(request, "⚠️ Có lỗi xảy ra! Vui lòng kiểm tra lại.")
            for field, error in form.errors.items():
                messages.error(request, f"{field}: {error}")
    else:
        form = FormHomestay()
    return render(request, 'create/create_homestay.html', {'form': form})

#UPDATE

#DELETE


