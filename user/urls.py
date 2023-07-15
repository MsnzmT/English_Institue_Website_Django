from django.urls import path
from user.views import *


urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('get/', get_users.as_view()),    
]

