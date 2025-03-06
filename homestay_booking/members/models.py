from django.db import models
from django.contrib.auth.models import User, AbstractUser # import thư viện AbstractUser

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE) # OneToOneField liên kết 1-1 với User đảm bảo 1user  chỉ có 1profile
    phoneNumber = models.CharField(max_length= 10, blank= True, null= True)
    avatar = models.ImageField(null= True, blank= True, upload_to= "images/")