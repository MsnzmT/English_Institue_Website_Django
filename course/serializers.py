from rest_framework import serializers
from .models import *
from user.models import Teacher
from rest_framework.relations import SlugRelatedField, StringRelatedField, HyperlinkedRelatedField


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
    
    class Meta:
        model = Course
        fields = ('id', 'title','short_description','course_image','price','teacher')


class CourseDetailSerializer(serializers.ModelSerializer):
    
    teacher = TeacherSerializer()
    previews = previewSerializer(many=True) 
    
    
    class Meta:
        model = Course
        fields = '__all__'