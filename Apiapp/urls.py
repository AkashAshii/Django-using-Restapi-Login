from django.urls import path
from .views import UserRegistrationAPIView, ListLoginRegAPIView, UserLoginAPIView

urlpatterns = [
    path('register/',UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('view/', ListLoginRegAPIView.as_view(), name='view'),
]


