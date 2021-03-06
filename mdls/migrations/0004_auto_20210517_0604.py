# Generated by Django 3.2.3 on 2021-05-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0003_auto_20210517_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdl',
            name='file',
            field=models.FileField(upload_to='mdls/obj', verbose_name='Файл модели'),
        ),
        migrations.AlterField(
            model_name='mdl',
            name='image',
            field=models.FileField(default=None, upload_to='mdls/img', verbose_name='Изображение модели'),
        ),
    ]
