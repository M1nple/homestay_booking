from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Homestay)
admin.site.register(HomestayImage)
admin.site.register(Review)
