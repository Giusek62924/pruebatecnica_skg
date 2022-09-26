from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class USERSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        read_only_fields = ('id',)