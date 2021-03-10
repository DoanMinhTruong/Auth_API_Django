from rest_framework import serializers
from .models import User 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('email' , 'username' , 'password','is_superuser')
        extra_kwargs = {'password': {'write_only': True}}