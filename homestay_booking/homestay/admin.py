from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Homestay)
admin.site.register(HomestayImage)
admin.site.register(Review)

@admin.register(TinhTP)
class TinhTPAdmin(admin.ModelAdmin):
    list_filter = ['ten']
    search_fields = ["ten"]

@admin.register(QuanHuyen)
class QuanHuyenAdmin(admin.ModelAdmin):
    list_display = ('ten', 'tinh_tp')
    list_filter = ('ten', 'tinh_tp')
    search_fields = ["ten", "tinh_tp__ten"] # tìm cả tên tình nma pahi __tencot trong db gjango băt làm the 


@admin.register(XaPhuong)
class XaPhuongAdmin(admin.ModelAdmin):
    list_display = ('ten', 'quan_huyen')
    list_filter = ('ten', 'quan_huyen')
    search_fields = ["ten", "quan_huyen__ten"] # tìm cả tên tình nma pahi __tencot trong db gjango băt làm the 



