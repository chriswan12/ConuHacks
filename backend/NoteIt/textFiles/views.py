from django.shortcuts import render
from django.http import HttpResponse
from textFiles.serializers import TextFilesSerializer
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from .models import TextFiles


# Create your views here.

class textFilesPut(CreateAPIView):
    queryset = TextFiles.objects.all()
    serializer_class = TextFilesSerializer


class textFilesView(ListCreateAPIView):
    queryset = TextFiles.objects.all()
    serializer_class = TextFilesSerializer
