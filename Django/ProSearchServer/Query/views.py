from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class gen_ques(APIView):
    def get(self, request):
     	return Response({"message": "this is a question"})
