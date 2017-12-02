from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from .serializer import  SeeSerializer
from .models import Questions

from .name_generator import generator
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

class SeeViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = SeeSerializer

    def get_queryset(self):
        queryset = Questions.objects.all()
        username = self.request.query_params.get('name', None)
        if username is not None:
            queryset = queryset.filter(name__name=username)
        return queryset


class gen_ques(APIView):
	def get(self, request, format=None):
		
		return Response({"answer": "school", 
        "question": "Students can be children, teenagers, or adults who are going to __________, but it may also be other people who are learning, such as in college or university.", 
        "similar_words": [
            "college", 
            "preschool", 
            "university"
        ], 
        "title": "student"
		})        




