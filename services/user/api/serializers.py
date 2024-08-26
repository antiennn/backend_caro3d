from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'