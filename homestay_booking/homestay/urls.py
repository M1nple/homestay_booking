from django.urls import path, include
from . import views 
 
urlpatterns = [
    # views
    path('', views.home, name= 'home'),
    path('list_homestay', views.list_homestay, name= 'list-homestay'),


    # create
    path('create_homestay', views.create_homestay, name= 'create-homestay')
]