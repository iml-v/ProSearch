from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from .serializer import  SeeSerializer
from .models import Questions

from .name_generator import generator


# Create your views here.

class SeeViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = SeeSerializer







