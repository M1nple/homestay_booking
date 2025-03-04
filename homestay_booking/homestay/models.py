from django.db import models
from django.contrib.auth.models import User, AbstractUser

# class User(AbstractUser):
# class User(AbstractUser):
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)



class TinhTP(models.Model):
    ten = models.CharField(max_length= 100, unique= True)
    def __str__(self):
        return self.ten

class QuanHuyen(models.Model):
    ten = models.CharField(max_length= 100)
    tinh_tp = models.ForeignKey(TinhTP, on_delete= models.CASCADE, related_name="quan_huyen")


    def __str__(self):
        return f"{self.ten} {self.tinh_tp}"
    
class XaPhuong(models.Model):
    ten = models.CharField(max_length=100)
    quan_huyen = models.ForeignKey(QuanHuyen, on_delete=models.CASCADE, related_name="xa_phuong")


    def __str__(self):
        return f"{self.ten} - {self.quan_huyen.ten} - {self.quan_huyen.tinh_tp.ten}"



class Homestay(models.Model):
    owner = models.IntegerField(blank= False, default= 1)
    homestay_name = models.CharField(max_length=255)
    homestay_address = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_rooms = models.IntegerField(default=1)
    decription = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HomestayImage(models.Model):
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="homestays/")

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 sao
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
