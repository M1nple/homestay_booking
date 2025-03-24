from django.urls import path
from . import views 

 
urlpatterns = [
    path('minh/', views.minh, name= 'minh'),

]