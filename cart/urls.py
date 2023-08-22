from django.urls import path, include
from cart.views import *

urlpatterns = [
    path('add/<int:course_id>/', AddDeleteCartView.as_view()),
    path('', UserCartView.as_view()),
    path('pay/', PayCartView.as_view()),
    path('discount/', DiscountView.as_view()),
]
