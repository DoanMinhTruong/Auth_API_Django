from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt import views as jwt_views
# Create your views here.
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            return JsonResponse(
                {'message': 'Register successfull!'}
            , status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(
                {'message': 'Register unsuccessfull!'}
            , status = status.HTTP_400_BAD_REQUEST)



def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(
            request,
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if user:
            refresh = jwt_views.TokenObtainPairSerializer.get_token(user)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }
            return JsonResponse(data, status=status.HTTP_200_OK)
            
        return JsonResponse({
            'error_message': 'Email or password is incorrect!',
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
        
    return JsonResponse({
        'error_messages': serializer.errors,
        'error_code': 400
    }, status=status.HTTP_400_BAD_REQUEST)