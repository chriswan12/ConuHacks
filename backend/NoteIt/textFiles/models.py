from django.db import models
# Create your models here.


def upload_path(instace, filename):
    print(filename)
    return '/'.join([filename])


class TextFiles(models.Model):
    file_upload = models.FileField(
        upload_to=upload_path, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.file_upload)
