from django.urls import path, include
from . import views 
 
urlpatterns = [
    path('', views.home, name= 'home'),

    # create
    path('create_homestay', views.create_homestay, name= 'create-homestay')
]