from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
# Create your views here.


class CourseView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'id'