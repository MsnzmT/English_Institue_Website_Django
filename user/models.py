from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    SEX_CHOICES = (
        ("مرد","مرد"),
        ("زن","زن")
    )
    
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    phone_number = models.CharField(max_length=11, unique=True)
    location = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True)
    
    def __str__(self):
        return self.username


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname