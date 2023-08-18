from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

User = get_user_model()



class cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='cart')
    course = models.ManyToManyField(Course , related_name='cart', blank=True)
    price = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)
    items = models.IntegerField(default=0)
    discount = models.ForeignKey('discount', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Cart of : ' + self.user.username
    
    
class discount(models.Model):
    code = models.CharField(max_length=10)
    percent = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    active = models.BooleanField(default=False)
    expire_date = models.DateTimeField()
    remaining = models.IntegerField()
    
    
    def __str__(self):
        return self.code
