from django.shortcuts import render
from rest_framework.views import APIView
from course.models import Course
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
# Create your views here.



class AddDeleteCartView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request, course_id):
        finded_course = Course.objects.get(id=course_id)
        user_cart = cart.objects.get(user=request.user)
        if finded_course in user_cart.course.all():
            return Response({"error":"tekrari hast"}, status=400)
        user_cart.course.add(finded_course)
        user_cart.price += finded_course.price
        user_cart.items += 1
        user_cart.save()
        return Response({"message":"ok"}, status=200)

    def delete(self, request, course_id):
        finded_course = Course.objects.get(id=course_id)
        user_cart = cart.objects.get(user=request.user)
        if finded_course not in user_cart.course.all():
            return Response({"error":"tush nist"}, status=400)
        user_cart.course.remove(finded_course)
        user_cart.price -= finded_course.price
        user_cart.items -= 1
        user_cart.save()
        return Response({"message":"ok"}, status=200)
    

class UserCartView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Cartserializer
    def get_object(self):
        return cart.objects.get(user=self.request.user)
    
    
class testView(APIView):
    def get(self, request):
        
        arabic = '۰۱۲۳۴۵۶۷۸۹'
        english = '0123456789'

        translation_table = str.maketrans(english, arabic)

        translated_num = "9956755308".translate(translation_table)
        return Response({"message":translated_num})