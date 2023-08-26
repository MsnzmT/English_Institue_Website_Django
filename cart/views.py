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
            return Response({"error":"این دوره در سبد خرید شما موجود هست"}, status=400)
        elif finded_course.users.filter(id=request.user.id).exists():
            return Response({"error":"شما قبلا این دوره را خریده اید"}, status=400)
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
    
    
class PayCartView(APIView):
    def put(self, request):
        finded_user = User.objects.get(id=request.user.id)
        finded_cart = cart.objects.get(user=request.user)
        if finded_cart.items == 0:
            return Response({"error":"سبد خرید شما خالی است"}, status=400)
        finded_user.courses.add(*finded_cart.course.all())
        finded_cart.course.clear()
        finded_cart.price = 0
        finded_cart.items = 0
        finded_cart.discount = None
        finded_cart.save()
        return Response({"message":"پرداخت شما با موفقیت انجام شد"}, status=200)


class DiscountView(APIView):
    def post(self, request):
        finded_discount = discount.objects.filter(code=request.data['discountcode'])
        if finded_discount.exists():
            finded_discount = finded_discount.first()
            if finded_discount.active:
                finded_cart = cart.objects.get(user=request.user)
                finded_cart.discount = finded_discount
                finded_cart.save()
                return Response({"message":"کد تخفیف با موفقیت اعمال شد"}, status=200)
            else:
                return Response({"error":"کد تخفیف منقضی شده است"}, status=400)
        else:
            return Response({"error":"کد تخفیف نامعتبر است"}, status=400)