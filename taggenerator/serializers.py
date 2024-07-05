from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class TagSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Tag
        fields = ['id', 'input']