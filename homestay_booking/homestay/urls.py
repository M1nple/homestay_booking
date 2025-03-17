from django.urls import path, include
from . import views 
from .views import *
 
urlpatterns = [
    # views
    path('', views.home, name= 'home'),
    path('list_homestay', views.list_homestay, name= 'list-homestay'),
    path('show_homestay <int:id>', views.show_homestay, name= 'show-homestay'),

    # create
    path('create_homestay', views.create_homestay, name= 'create-homestay'),

    # Update
    path('update_homestay/<int:id> ', views.update_homestay, name= 'update-homestay'),

    # Delete
    path('delete_img/<int:id> ', views.deleteImage, name= 'delete-image'),


    #API
    path("api/quan-huyen/", get_quan_huyen, name="api_quan_huyen"),
    path("api/xa-phuong/", get_xa_phuong, name="api_xa_phuong"),
    path("form/", form_view, name="form"),



]