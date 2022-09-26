from rest_framework import serializers

from .models import *

class MASTERSerializer(serializers.ModelSerializer):
    class Meta:
        model = MASTER
        fields = ('entity','role','city')
        read_only_fields = ('id',)