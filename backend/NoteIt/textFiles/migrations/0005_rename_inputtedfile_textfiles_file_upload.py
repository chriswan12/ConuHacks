# Generated by Django 4.0.1 on 2022-01-30 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textFiles', '0004_remove_textfiles_file_upload_textfiles_inputtedfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textfiles',
            old_name='inputtedFile',
            new_name='file_upload',
        ),
    ]