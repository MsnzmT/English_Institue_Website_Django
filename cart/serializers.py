from rest_framework import serializers
from .models import *
from course.serializers import CourseSerializer
from persiantools.digits import en_to_fa


class PersianIntegerField(serializers.Field):
    def to_representation(self, value):
        return en_to_fa(str(value))

class Cartserializer(serializers.ModelSerializer):
    
    #course = serializers.StringRelatedField(many=True)
    course = CourseSerializer(many=True)
    price = PersianIntegerField()
    items = PersianIntegerField()
    final_price = PersianIntegerField()
    discount_price = PersianIntegerField()
    
    class Meta:
        model = cart
        fields = ('items', 'price', 'course', 'final_price', 'discount_price')
    