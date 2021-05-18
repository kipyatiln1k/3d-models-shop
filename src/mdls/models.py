import os
from django.db import models

from kolyma_store.settings import BASE_DIR


class Tag(models.Model):
        """Категория модели"""
        name = models.CharField(max_length=50, unique=True, verbose_name='Категория')
    
    
        class Meta:
            """Meta definition for Tag."""
    
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'
            ordering = ['name']
    
        def __str__(self):
            return self.name



class Mdl(models.Model):
    """Определение модели для Mdl (3D Model)."""
    
    # TODO: Define fields here
    
    name = models.CharField(max_length=50, verbose_name='Модель')
    description = models.TextField(editable=True, verbose_name='Описание модели')
    date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата добавления')
    file = models.FileField(upload_to='mdls/obj', verbose_name='Файл модели')
    tags = models.ManyToManyField(Tag, verbose_name='Категории модели', related_name='model_tags')
    extension = models.CharField(max_length=10, default='.fbx', auto_created=True, verbose_name='Расширение модели')
    image = models.ImageField(upload_to='mdls/img', verbose_name='Изображение модели', default=None)


    class Meta:
        """Meta definition for Mdl."""

        verbose_name = 'Модель'         
        verbose_name_plural = 'Модели'
        ordering = ['date', 'name']  

    def __str__(self):
        return self.name

    # def save(self):
    #     """Save method for Mdl."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Mdl."""
    #     return ('')

    # TODO: Define custom methods here
    
    
    