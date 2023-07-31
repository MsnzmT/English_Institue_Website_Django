from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView 
from .serializers import *
from djoser.serializers import TokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



class SignUp(APIView):
    
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response(TokenSerializer(token).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def UserView(request):
    return Response(UserSerializer(request.user).data)