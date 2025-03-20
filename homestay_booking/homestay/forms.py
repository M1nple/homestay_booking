from django import forms
from .models import *

# class FormHomestay(forms.ModelForm):
#     # tinh = forms.ModelChoiceField(queryset=TinhTP.objects.all(), empty_label="-- Chọn tỉnh --", required=True)
#     # quan = forms.ModelChoiceField(queryset=QuanHuyen.objects.none(), empty_label="-- Chọn quận/huyện --", required=True)
#     # xa = forms.ModelChoiceField(queryset=XaPhuong.objects.none(), empty_label="-- Chọn xã/phường --", required=True)
#     class Meta:
#         model = Homestay
#         fields = ('homestay_name', 'homestay_address', 'price_per_night', 'total_rooms', 'decription', 'tinh_tp', 'quan_huyen', 'xa_phuong')
#         labels = {
#                   'homestay_name': 'Tên homestay', 
#                   'homestay_address': "địa chỉ", 
#                   'price_per_night': 'giá 1 đêm', 
#                   'total_rooms': 'số phòng' , 
#                   'decription': 'mô tả',
#         }


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['homestay_name'].widget.attrs.update({
#             'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#             'placeholder' : 'test ten homestay',
#             'id' : 'homestay_name'
#         })

#         self.fields['homestay_address'].widget.attrs.update({
#             'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#             'placeholder' : 'dia chi',
#             'id' : 'homestay_address'
#         })
#         self.fields['price_per_night'].widget.attrs.update({
#             'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#             'placeholder' : 'giá tiền',
#             'id' : 'price_per_night'
#         })
#         self.fields['total_rooms'].widget.attrs.update({
#             'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#             'placeholder' : 'số lượng phòng',
#             'id' : 'total_rooms'
#         })
#         self.fields['decription'].widget.attrs.update({
#             'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
#             'placeholder' : 'mô tả',
#             'id' : 'decription'
#         })

class FormHomestayImage(forms.ModelForm):
    class Meta:
        model = HomestayImage
        fields =('image',)

        

class FormHomestay(forms.ModelForm):
    tinh_tp = forms.ModelChoiceField(
        queryset=TinhTP.objects.all(), 
        empty_label="-- Chọn tỉnh --"
    )
    # Ban đầu để queryset trống, sau đó sẽ cập nhật lại nếu có instance
    quan_huyen = forms.ModelChoiceField(
        queryset=QuanHuyen.objects.none(), 
        empty_label="-- Chọn quận/huyện --", 
        required=False
    )
    xa_phuong = forms.ModelChoiceField(
        queryset=XaPhuong.objects.none(), 
        empty_label="-- Chọn xã/phường --", 
        required=False
    )
    
    class Meta:
        model = Homestay
        fields = ('homestay_name', 'tinh_tp', 'quan_huyen', 'xa_phuong', 
                  'homestay_address', 'price_per_night', 'total_rooms', 'decription')
        labels = {
            'homestay_name': 'Tên homestay', 
            'tinh_tp': 'Tỉnh Thành Phố',
            'quan_huyen': 'Quận Huyện',
            'xa_phuong': 'Xã Phường',
            'homestay_address': "Địa chỉ", 
            'price_per_night': 'Giá 1 đêm', 
            'total_rooms': 'Số phòng', 
            'decription': 'Mô tả',
        }





    def __init__(self, *args, **kwargs):
        super(FormHomestay, self).__init__(*args, **kwargs)
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
        self.fields['tinh_tp'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'id' : 'tinh',
            'name' : 'tinh_tp'
        })
        self.fields['quan_huyen'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'id' : 'quan',
            'name': 'quan_huyen'
            
        })
        self.fields['xa_phuong'].widget.attrs.update({
            'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'id' : 'xa',
            'name': 'xa_phuong'
        })

 # Cập nhật danh sách Tỉnh
        self.fields['tinh_tp'].queryset = TinhTP.objects.all()
        
        # Mặc định để trống (chờ dữ liệu)
        self.fields['quan_huyen'].queryset = QuanHuyen.objects.none()
        self.fields['xa_phuong'].queryset = XaPhuong.objects.none()

        # Nếu có dữ liệu từ instance (trường hợp cập nhật)
        if self.instance.pk:
            self.fields['quan_huyen'].queryset = QuanHuyen.objects.filter(tinh_tp=self.instance.tinh_tp)
            self.fields['xa_phuong'].queryset = XaPhuong.objects.filter(quan_huyen=self.instance.quan_huyen)

        # Nếu dữ liệu gửi lên có tỉnh/huyện, cập nhật queryset
        if 'tinh_tp' in self.data:
            try:
                tinh_tp_id = int(self.data.get('tinh_tp'))
                self.fields['quan_huyen'].queryset = QuanHuyen.objects.filter(tinh_tp_id=tinh_tp_id)
            except (ValueError, TypeError):
                pass  # Nếu lỗi, để queryset rỗng
        
        if 'quan_huyen' in self.data:
            try:
                quan_huyen_id = int(self.data.get('quan_huyen'))
                self.fields['xa_phuong'].queryset = XaPhuong.objects.filter(quan_huyen_id=quan_huyen_id)
            except (ValueError, TypeError):
                pass  # Nếu lỗi, để queryset rỗng
