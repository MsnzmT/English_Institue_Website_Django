from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import status



class SignUp(APIView):
    def post(self, request):
        username = request.data['username']
        pass1 = request.data['password1']
        pass2 = request.data['password2']
        email = request.data['email']
        full_name = request.data['full_name']
        users = CustomUser.objects.filter(username=username)
        if users.exists():
            return Response(status=status.HTTP_409_CONFLICT)
        if pass2 != pass1:
            return Response({'message': 'Entered passwords are not identical'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            CustomUser.objects.create_user(username=username, password=pass1, email=email,
                                           full_name=full_name)
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)