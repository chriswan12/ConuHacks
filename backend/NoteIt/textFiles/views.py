from turtle import settiltangle
from django.conf import settings
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

    def post(self, request, *args, **kwargs):
        try:
            file_upload = request.data['file_upload']
            TextFiles.objects.create(file_upload=file_upload)
            return HttpResponse({'message': 'text-file uploaded'}, status=200)
        except:
            return HttpResponse({'message': 'text-file failed'}, status=400)


class textFilesView(ListCreateAPIView):
    queryset = TextFiles.objects.all()
    serializer_class = TextFilesSerializer
