from django.shortcuts import render
from django.http import HttpResponse
from textFiles.serializers import TextFilesSerializer
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView
from .models import TextFiles


# Create your views here.

class textFilesView(CreateAPIView):
    queryset = TextFiles.objects.all()
    serializer_class = TextFilesSerializer
