from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .serializers import Tinh_tp_serializers, Quan_huyen_serializers, Xa_phuong_serializers, User_serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse  # api
from rest_framework import viewsets
from django.contrib import messages
from .forms import *
from .models import *


# VIEWS
def home(request):
    homestays = Homestay.objects.all()
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'homestays/home.html', {'homestays': homestays})


@login_required(login_url='login')
def list_homestay(request):
    me = request.user
    homestays = Homestay.objects.filter(owner=me).prefetch_related("images")
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'homestays/list_homestay.html', {'homestays': homestays})


@login_required(login_url='login')
def show_homestay(request, id):
    homestays = Homestay.objects.filter(id=id)
    images = HomestayImage.objects.filter(homestay=id)

    return render(request, 'homestays/show_homestay.html', {'homestays': homestays, 'images': images})


# CREATE
@login_required(login_url='login')
def create_homestay(request):
    ds_tinh = TinhTP.objects.all()  # Chỉ load danh sách Tỉnh/Thành phố
    if request.method == "POST":
        form = FormHomestay(request.POST)
        # vì nó ở 1 model riêng nên kh thêm được vào form nên sẽ tạo input ở trang html và đặt name cho nó r gọi vào
        files = request.FILES.getlist("images")
        if form.is_valid():
            homestay = form.save(commit=False)

            quan_huyen = form.cleaned_data.get("quan_huyen")
            xa_phuong = form.cleaned_data.get("xa_phuong")
            if not quan_huyen or not xa_phuong:
                messages.error(request, ("chọn quận huyên / phường xã "))
                return redirect("create-homestay")
                # return render(request, 'homestays/create_homestay.html', {'form': form, "ds_tinh": ds_tinh})

            # chưa lưu vào db luôn
            homestay.owner = request.user

            # sau đó mới lưu
            homestay.save()
            for file in files:  # lấy từng ảnh trong đống ảnh inport lên
                # lưu vào homestay = id của bảng homestay image = file vừa upload lên
                HomestayImage.objects.create(homestay=homestay, image=file)
            messages.success(request, "them thanh cong")
            return redirect('home')
        else:
            messages.error(request, "⚠️ Có lỗi xảy ra! Vui lòng kiểm tra lại.")
            for field, error in form.errors.items():
                messages.error(request, f"{field}: {error}")
    else:
        form = FormHomestay()
    return render(request, 'homestays/create_homestay.html', {'form': form, "ds_tinh": ds_tinh})


# UPDATE
@login_required(login_url='login')
def update_homestay(request, id):
    homestay = get_object_or_404(Homestay, pk=id)
    ds_tinh = TinhTP.objects.all()  # Chỉ load danh sách Tỉnh/Thành phố

    # Nếu người dùng không phải chủ của homestay, chuyển hướng về trang chủ
    if request.user != homestay.owner:
        return redirect("home")

    if request.method == "POST":
        form = FormHomestay(request.POST, instance=homestay)
        files = request.FILES.getlist("images")  # Lấy danh sách ảnh mới

        if form.is_valid():  # Lấy dữ liệu đã xác thực từ form
            form.save(commit=False)

            quan_huyen = form.cleaned_data.get("quan_huyen")
            xa_phuong = form.cleaned_data.get("xa_phuong")
            if not quan_huyen or not xa_phuong:  # đảm bảo 2 trường này kh null
                messages.error(request, ("chọn quận huyên / phường xã "))
                return redirect('update-homestay', id=id)
                # return render(request, 'homestays/create_homestay.html', {'form': form, "ds_tinh": ds_tinh})

            form.save()

            # Xóa ảnh cũ nếu người dùng chọn xóa ảnh
            if "delete_images" in request.POST:
                HomestayImage.objects.filter(homestay=homestay).delete()

            # Thêm ảnh mới
            for file in files:
                HomestayImage.objects.create(homestay=homestay, image=file)

            # Chuyển hướng sau khi cập nhật thành công
            return redirect("list-homestay")
    else:
        form = FormHomestay(instance=homestay)

    images = HomestayImage.objects.filter(
        homestay=homestay)  # Lấy tất cả ảnh của homestay

    return render(request, "homestays/update_homestay.html", {
        "form": form,
        "images": images,
        "ds_tinh": ds_tinh
    })


# DELETE
@login_required(login_url='login')
def deleteImage(request, id):
    # ✅ Lấy ảnh hoặc 404 nếu không có
    image = get_object_or_404(HomestayImage, id=id)
    # image = HomestayImage.objects.get(id=id)
    homestay = image.homestay
    if request.user == homestay.owner:
        image.image.delete()  # ✅ Xóa file ảnh trong thư mục media/
        image.delete()  # ✅ Xóa record khỏi database
        messages.success(request, ('xóa thành công'))
    else:
        messages.error(request, ('lôix '))
    return redirect("update-homestay", id=homestay.id)


@login_required(login_url='login')
def deleteHomestay(request, id):
    homestay = get_object_or_404(Homestay, pk=id)

    if request.user != homestay.owner:
        messages.error(request, "Bạn không có quyền xóa homestay này!")
        return redirect("list-homestay")

    if request.method == "POST":
        password = request.POST.get("password")  # Lấy mật khẩu từ form

        user = authenticate(
            request, username=request.user.username, password=password)
        if user:  # Nếu mật khẩu đúng, thực hiện xóa
            homestay.delete()
            messages.success(request, "Xóa thành công")
            return redirect("list-homestay")
        else:  # Nếu sai mật khẩu, báo lỗi
            messages.error(request, "Mật khẩu không đúng!")

    return render(request, "homestays/confirm_delete_homestay.html", {"homestay": homestay})


# API

class tinh_tp_APIView(viewsets.ModelViewSet):
    queryset = TinhTP.objects.all()
    serializer_class = Tinh_tp_serializers


class quan_huyen_APIView(viewsets.ModelViewSet):
    queryset = QuanHuyen.objects.all()
    serializer_class = Quan_huyen_serializers


class xa_phuong_APIView(viewsets.ModelViewSet):
    queryset = XaPhuong.objects.all()
    serializer_class = Xa_phuong_serializers


class user_APIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializers


def get_quan_huyen(request):
    tinh_id = request.GET.get("tinh_id")
    if tinh_id:
        quan_huyen = QuanHuyen.objects.filter(
            tinh_tp_id=tinh_id).values("id", "ten")
        return JsonResponse(list(quan_huyen), safe=False)
    return JsonResponse([])


def get_xa_phuong(request):
    quan_id = request.GET.get("quan_id")
    if quan_id:
        xa_phuong = XaPhuong.objects.filter(
            quan_huyen_id=quan_id).values("id", "ten")
        return JsonResponse(list(xa_phuong), safe=False)
    return JsonResponse([])
