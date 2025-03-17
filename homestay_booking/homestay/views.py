from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse # api
from django.contrib import messages
from .forms import *
from .models import *






#VIEWS
def home(request):
    homestays = Homestay.objects.all()
    return render(request, 'home.html', {'homestays': homestays})

@login_required(login_url='login')
def list_homestay(request):
    me = request.user
    homestays = Homestay.objects.filter(owner = me).prefetch_related("images") 
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'views/list_homestay.html',{'homestays': homestays})

@login_required(login_url='login')
def show_homestay(request, id ):
    homestay = Homestay.objects.filter(id = id )
    images = HomestayImage.objects.filter(homestay = id)
    return render(request, 'views/show_homestay.html', {'homestays': homestay, 'images': images})


#CREATE
@login_required(login_url='login')
def create_homestay(request):
    ds_tinh = TinhTP.objects.all()  # Chỉ load danh sách Tỉnh/Thành phố
    if request.method == "POST":
        form = FormHomestay(request.POST) 
        files = request.FILES.getlist("images") #vì nó ở 1 model riêng nên kh thêm được vào form nên sẽ tạo input ở trang html và đặt name cho nó r gọi vào 
        if form.is_valid():
            
            # lấy dữ liêu qua name từ template sang
            tinh = form.cleaned_data['tinh_tp']
            huyen = form.cleaned_data['quan_huyen']
            xa = form.cleaned_data['xa_phuong']

            # chưa lưu vào db luôn 
            homestay = form.save(commit=False)

            # gán các biến vào db 
            homestay.tinh_tp = tinh
            homestay.quan_huyen = huyen
            homestay.xa_phuong = xa
            homestay.owner = request.user
            
            # sau đó mới lưu
            homestay.save()
            for file in files: # lấy từng ảnh trong đống ảnh inport lên 
                HomestayImage.objects.create(homestay = homestay, image = file) # lưu vào homestay = id của bảng homestay image = file vừa upload lên 
            messages.success(request,"them thanh cong")
            return redirect('home')
        else:
            messages.error(request, "⚠️ Có lỗi xảy ra! Vui lòng kiểm tra lại.")
            for field, error in form.errors.items():
                messages.error(request, f"{field}: {error}")
    else:
        form = FormHomestay()
    return render(request, 'create/create_homestay.html', {'form': form, "ds_tinh": ds_tinh})

#UPDATE


@login_required(login_url='login')
def update_homestay(request, id):
    homestay = get_object_or_404(Homestay, pk=id)

    if request.user != homestay.owner:
        return redirect("home")  # ✅ Nếu không phải chủ homestay, quay về trang chính
 
    if request.method == "POST":
        form = FormHomestay(request.POST, instance=homestay)
        ds_tinh = TinhTP.objects.all()  # Chỉ load danh sách Tỉnh/Thành phố
        files = request.FILES.getlist("images")  # ✅ Lấy danh sách ảnh mới

        if form.is_valid():
            form.save()  # ✅ Cập nhật thông tin homestay

            # ✅ Xóa ảnh cũ nếu cần
            if "delete_images" in request.POST:  # Nếu người dùng chọn xóa ảnh
                HomestayImage.objects.filter(homestay=homestay).delete()

            # ✅ Thêm ảnh mới vào bảng HomestayImage
            for file in files:
                HomestayImage.objects.create(homestay=homestay, image=file)

            return redirect("list-homestay")  # ✅ Chuyển hướng sau khi cập nhật thành công

    else:
        form = FormHomestay(instance=homestay)

    images = HomestayImage.objects.filter(homestay=homestay)  # ✅ Lấy tất cả ảnh của homestay

    return render(request, "update/update_homestay.html", {"form": form, "images": images, "ds_tinh": ds_tinh})


#DELETE
@login_required(login_url='login')
def deleteImage(request, id):
    image = get_object_or_404(HomestayImage, id=id)  # ✅ Lấy ảnh hoặc 404 nếu không có
    # image = HomestayImage.objects.get(id=id)
    homestay = image.homestay
    if request.user == homestay.owner:        
        image.image.delete()  # ✅ Xóa file ảnh trong thư mục media/
        image.delete()  # ✅ Xóa record khỏi database
        messages.success(request,('xóa thành công'))
    else:
        messages.error(request, ('lôix '))
    return redirect("update-homestay", id=homestay.id)



#API

def get_quan_huyen(request):
    tinh_id = request.GET.get("tinh_id")
    if tinh_id:
        quan_huyen = QuanHuyen.objects.filter(tinh_tp_id = tinh_id).values("id", "ten")
        return JsonResponse(list(quan_huyen), safe=False)
    return JsonResponse([])

def get_xa_phuong(request):
    quan_id = request.GET.get("quan_id")
    if quan_id:
        xa_phuong = XaPhuong.objects.filter(quan_huyen_id = quan_id).values("id", "ten")
        return JsonResponse(list(xa_phuong), safe= False)
    return JsonResponse([])



def form_view(request):
    ds_tinh = TinhTP.objects.all()  # Chỉ load danh sách Tỉnh/Thành phố
    return render(request, "views/form.html", {"ds_tinh": ds_tinh})
