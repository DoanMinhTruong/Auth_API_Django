from django.urls import path 
from .views import *
from rest_framework_simplejwt import views as jwt_views 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('register' , UserRegisterView.as_view() , name = 'register' ),
    path('login' , jwt_views.TokenObtainPairView.as_view() , name='login'),
    path('token/refresh' , TokenRefreshView.as_view() , name = 'token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]