from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseView.as_view()),
    path('<int:id>/', CourseDetailView.as_view()),
    # path('thisuser/', UserCourseView.as_view()),
] 