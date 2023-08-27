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
        lang = self.request.query_params.getlist("languages")
        if not prof and not lang:
            return Course.objects.all()
        elif not lang:
            q_object = Q()
            for prof_name in prof:
                q_object |= Q(teacher__fullname=prof_name)
            return Course.objects.filter(q_object)
        elif not prof:
            q_object = Q()
            for lang_name in lang:
                q_object |= Q(language=lang_name)
            return Course.objects.filter(q_object)
        else:
            q_object = Q()
            q_object1 = Q()
            q_object2 = Q()
            for prof_name in prof:
                q_object1 |= Q(teacher__fullname=prof_name)
            for lang_name in lang:
                q_object2 |= Q(language=lang_name)
            q_object = q_object1 & q_object2
            return Course.objects.filter(q_object)