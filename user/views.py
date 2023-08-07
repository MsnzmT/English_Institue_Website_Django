from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView , UpdateAPIView
from .serializers import *
from djoser.serializers import TokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.dispatch import receiver



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



class EditUserView(UpdateAPIView):
    serializer_class = EditUserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    send_mail(
        # title:
        "پشتیبانی زبان لرن - فراموشی رمز عبور",
        # message:
        f"سلام\nکد یکبار مصرف شما {reset_password_token.key} می باشد.\nهشدار : لطفا از در اختیار دادن کد به دیگران جدا خودداری نمایید.\n\n با احترام\nتیم پشتیبانی زبان لرن",
        # from:
        "zabanlearn@support.mohsenzahmatkesh.ir",
        # to:
        [reset_password_token.user.email]
    )