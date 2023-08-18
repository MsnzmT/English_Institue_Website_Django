from django.shortcuts import render
from front.models import *
from front.serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.



class GetOptionView(APIView):
    def get(self, request, key):
        option = get_object_or_404(Option, key=key)
        serializer = OptionSerializer(option)
        return Response(serializer.data)