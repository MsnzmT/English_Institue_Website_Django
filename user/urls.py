from django.urls import path, include
from user.views import *

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('', include('djoser.urls.authtoken')),
    path('me/', UserView),
    path('edit/', EditUserView.as_view()),
]

