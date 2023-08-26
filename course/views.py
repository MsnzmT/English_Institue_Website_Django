from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CourseView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'id'



class UserCourseView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(users=user)


class FilterCourse(ListAPIView):
    serializer_class = CourseSerializer
    def get_queryset(self):
        prof = self.request.query_params.get('teachers')
        if prof == "":
            return Course.objects.all()
        return Course.objects.filter(teacher__fullname=prof)