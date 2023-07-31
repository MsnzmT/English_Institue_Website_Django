from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.username


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name