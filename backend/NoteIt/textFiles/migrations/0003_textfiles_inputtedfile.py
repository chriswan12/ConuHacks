# Generated by Django 4.0.1 on 2022-01-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textFiles', '0002_remove_textfiles_inputtedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfiles',
            name='inputtedFile',
            field=models.FileField(default='hello.txt', upload_to=''),
        ),
    ]
