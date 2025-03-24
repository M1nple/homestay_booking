from rest_framework import serializers # import thư viện
from django.contrib.auth.models import User
from .models import * #import models

class Tinh_tp_serializers(serializers.ModelSerializer):
    class Meta:
        model = TinhTP
        fields = '__all__' #    lấy tất cả hoạc có thể liệt kê ra chỉ các bảng muốn lấy 

class Quan_huyen_serializers(serializers.ModelSerializer):
    class Meta:
        model = QuanHuyen
        fields = '__all__'

class Xa_phuong_serializers(serializers.ModelSerializer):
    class Meta:
        model = XaPhuong
        fields = '__all__'

class User_serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'