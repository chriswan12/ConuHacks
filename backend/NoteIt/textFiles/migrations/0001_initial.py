# Generated by Django 4.0.1 on 2022-01-30 06:24

from django.db import migrations, models
import textFiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.FileField(blank=True, null=True, upload_to=textFiles.models.upload_path)),
                ('useremail', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]
