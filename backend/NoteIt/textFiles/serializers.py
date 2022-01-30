from rest_framework import serializers
from .models import TextFiles


class TextFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFiles
        fields = ('file_upload', 'id', 'useremail')
