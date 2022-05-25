from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login')

class TodoSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Todolist
        fields = ('__all__')