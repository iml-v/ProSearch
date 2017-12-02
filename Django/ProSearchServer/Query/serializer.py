from rest_framework import serializers
from .models import Questions

class SeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('name' , 'question','query')

