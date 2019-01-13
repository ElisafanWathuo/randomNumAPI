from rest_framework import serializers
from .models import RandomNum
import random

class RandomNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomNum
        fields = '__all__'