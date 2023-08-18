from rest_framework import serializers
from .models import *
from user.models import Teacher
from rest_framework.relations import SlugRelatedField, StringRelatedField, HyperlinkedRelatedField
from persiantools.digits import en_to_fa

class PersianIntegerField(serializers.Field):
    def to_representation(self, value):
        return en_to_fa(str(value))


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('fullname','teacher_image', 'description', 'subtitle')
        
class previewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = ('title','video')


class CourseSerializer(serializers.ModelSerializer):
    
    teacher = TeacherSerializer()
    price = PersianIntegerField()
    
    class Meta:
        model = Course
        fields = ('id', 'title','short_description','course_image','price','teacher')


class CourseDetailSerializer(serializers.ModelSerializer):
    
    teacher = TeacherSerializer()
    previews = previewSerializer(many=True)
    price = PersianIntegerField()
    number_of_students = PersianIntegerField()
    number_of_sessions = PersianIntegerField()
    duration = PersianIntegerField()
    
    
    
    
    class Meta:
        model = Course
        fields = ('teacher', 'previews', 'title', 'description', 'short_description', 'course_image', 'price', 'number_of_students', 'number_of_sessions', 'duration', 'content')