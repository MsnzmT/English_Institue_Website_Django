from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
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
        prof = self.request.query_params.getlist("teachers")
        if not prof:
            return Course.objects.all()
        q_object = Q()
        for prof_name in prof:
            q_object |= Q(teacher__fullname=prof_name)
        return Course.objects.filter(q_object)