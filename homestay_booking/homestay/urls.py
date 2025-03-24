from django.urls import path, include
from . import views 
from .views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import tinh_tp_APIView
 
# Tạo router
router = DefaultRouter() # Khởi tạo router
router.register(r'tinh_tp', tinh_tp_APIView )  # Đăng ký ViewSet, tạo endpoint /api/homestays/
router.register(r'quan_huyen', quan_huyen_APIView)
router.register(r'xa_phuong', xa_phuong_APIView)
router.register(r'user', user_APIView)




urlpatterns = [
   #API
    path('api/', include(router.urls)),  # Định tuyến API, Gộp các URL tự động tạo vào API

    path("api/quan-huyen/", get_quan_huyen, name="api_quan_huyen"),
    path("api/xa-phuong/", get_xa_phuong, name="api_xa_phuong"),
    # views
    path('', views.home, name= 'home'),
    path('list_homestay', views.list_homestay, name= 'list-homestay'),
    path('show_homestay/<int:id>', views.show_homestay, name= 'show-homestay'),
    
    # create
    path('create_homestay', views.create_homestay, name= 'create-homestay'),

    # Update
    path('update_homestay/<int:id> ', views.update_homestay, name= 'update-homestay'),

    # Delete
    path('delete_img/<int:id> ', views.deleteImage, name= 'delete-image'),
    path('delete_homestay/<int:id>', views.deleteHomestay, name = 'delete-homestay'),
    


    
]