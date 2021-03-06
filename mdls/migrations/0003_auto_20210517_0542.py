# Generated by Django 3.2.3 on 2021-05-17 02:42

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0002_auto_20210517_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdl',
            name='file',
            field=models.FileField(upload_to=pathlib.PureWindowsPath('E:/Работа для Коловрата/KolymaStore/src/media/mdls_files/obj'), verbose_name='Файл модели'),
        ),
        migrations.AlterField(
            model_name='mdl',
            name='image',
            field=models.FileField(default=None, upload_to=pathlib.PureWindowsPath('E:/Работа для Коловрата/KolymaStore/src/media/mdls_files/img'), verbose_name='Изображение модели'),
        ),
    ]
