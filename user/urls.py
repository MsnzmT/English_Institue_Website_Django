from django.urls import path
from user.views import *


urlpatterns = [
    path('signup/', SignUp.as_view()),    
]

