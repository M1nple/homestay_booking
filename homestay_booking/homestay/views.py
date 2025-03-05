from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import*

# Create your views here.
def home(request):
    homestays = Homestay.objects.all()
    return render(request, 'home.html', {'homestays': homestays})


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
            messages.error(request,"loi")
    else:
        form = FormHomestay()
    return render(request, 'create/create_homestay.html', {'form': form})



