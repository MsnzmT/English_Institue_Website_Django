from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    SEX_CHOICES = (
        ("مرد","مرد"),
        ("زن","زن")
    )
    
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True)
    phone_number = models.CharField(max_length=11, unique=True, null=True)
    location = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    teacher_image = models.ImageField(upload_to='teacher_image', null=True)
    description = models.TextField(null=True)
    subtitle = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.fullname