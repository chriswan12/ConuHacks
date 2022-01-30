from django.db import models

# Create your models here.


class TextFiles(models.Model):
    inputtedFile = models.FileField(default="hello.txt")
