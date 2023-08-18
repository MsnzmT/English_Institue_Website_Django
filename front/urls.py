from django.urls import path
from . import views

urlpatterns = [
    path('get_option/<key>', views.GetOptionView.as_view()),
]
