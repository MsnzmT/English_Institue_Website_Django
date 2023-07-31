from django.urls import path, include
from user.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('', include('djoser.urls.authtoken')),
    path('me/', UserView),
]

