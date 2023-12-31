from django.db import models
from user.models import Teacher
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Course(models.Model):
    
    LANGUAGE_CHOICES = (
        ('فرانسوی','فرانسوی'),
        ('انگلیسی','انگلیسی'),
        ('آلمانی','آلمانی'),
        ('اسپانیایی','اسپانیایی'),
        ('عربی','عربی'),
        ('روسی','روسی'),
    )
    
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True, related_name='courses')
    title = models.CharField(max_length=90)
    description = models.TextField(null=True)
    short_description = models.CharField(max_length=50, null=True)
    course_image = models.ImageField(upload_to='course_image', null=True)
    price = models.IntegerField(null=True)
    number_of_students = models.IntegerField(default=0)
    number_of_sessions = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    content = models.TextField(null=True)
    language = models.CharField(max_length=30, null=True, blank=True, choices=LANGUAGE_CHOICES)
    
    
    
    def __str__(self):
        return self.title
    


class Preview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='previews')
    video = models.FileField(upload_to='preview_video')
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title