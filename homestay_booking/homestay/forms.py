from django import forms
from .models import *

class FormHomestay(forms.ModelForm):
    # tinh = forms.ModelChoiceField(queryset=TinhTP.objects.all(), empty_label="-- Chọn tỉnh --", required=True)
    # quan = forms.ModelChoiceField(queryset=QuanHuyen.objects.none(), empty_label="-- Chọn quận/huyện --", required=True)
    # xa = forms.ModelChoiceField(queryset=XaPhuong.objects.none(), empty_label="-- Chọn xã/phường --", required=True)
    class Meta:
        model = Homestay
        fields = ('homestay_name', 'homestay_address', 'price_per_night', 'total_rooms', 'decription', 'tinh_tp', 'quan_huyen', 'xa_phuong')
        labels = {
                  'homestay_name': 'Tên homestay', 
                  'homestay_address': "địa chỉ", 
                  'price_per_night': 'giá 1 đêm', 
                  'total_rooms': 'số phòng' , 
                  'decription': 'mô tả',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['homestay_name'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder' : 'test ten homestay',
            'id' : 'homestay_name'
        })

        self.fields['homestay_address'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder' : 'dia chi',
            'id' : 'homestay_address'
        })
        self.fields['price_per_night'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder' : 'giá tiền',
            'id' : 'price_per_night'
        })
        self.fields['total_rooms'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder' : 'số lượng phòng',
            'id' : 'total_rooms'
        })
        self.fields['decription'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder' : 'mô tả',
            'id' : 'decription'
        })

class FormHomestayImage(forms.ModelForm):
    class Meta:
        model = HomestayImage
        fields =('image',)