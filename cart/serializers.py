from rest_framework import serializers
from .models import *
from course.serializers import CourseSerializer




class Cartserializer(serializers.ModelSerializer):
    
    #course = serializers.StringRelatedField(many=True)
    course = CourseSerializer(many=True)
    
    class Meta:
        model = cart
        fields = ('items', 'price', 'course')
    