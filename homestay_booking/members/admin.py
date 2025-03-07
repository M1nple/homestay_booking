from django.contrib import admin
from . models import *
# Register your models here.
# admin.site.register(UserProfile)

@admin.register(UserProfile)
class QuanHuyenAdmin(admin.ModelAdmin):
    list_display = ('user', 'phoneNumber', 'avatar')
    list_filter = ('user', 'phoneNumber')
    search_fields = ["ten", "tinh_tp__ten"] # tìm cả tên tình nma pahi __tencot trong db gjango băt làm the 