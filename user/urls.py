from django.urls import path
from user.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('login/', view=obtain_auth_token),
]

