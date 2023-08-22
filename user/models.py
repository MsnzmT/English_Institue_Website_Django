from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

def validate_phone(value):
    if not value.isdigit():
        raise ValidationError('شماره موبایل وارد شده عدد نیست')
    elif len(value) > 11:
        raise ValidationError('شماره موبایل وارد شده بیش از 11 رقم است')
    elif len(value) < 11:
        raise ValidationError('شماره موبایل وارد شده کمتر از 11 رقم است')


class CustomUser(AbstractUser):
    SEX_CHOICES = (
        ("مرد","مرد"),
        ("زن","زن")
    )
    
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True)
    phone_number = models.CharField(max_length=110, unique=True, null=True, blank=True,validators=[validate_phone], error_messages={
        "unique": ("این شماره موبایل از قبل در سیستم ثبت شده است")
    })
    location = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True)
    email = models.EmailField(unique=True, error_messages={"unique": ("این ایمیل از قبل در سیستم ثبت شده است")})
    
    def __str__(self):
        return self.username


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    teacher_image = models.ImageField(upload_to='teacher_image', null=True)
    description = models.TextField(null=True)
    subtitle = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.fullname