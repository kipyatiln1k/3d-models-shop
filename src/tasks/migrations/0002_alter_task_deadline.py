# Generated by Django 3.2.3 on 2021-05-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default='2021-05-24 00:56:11.510827', verbose_name='Срок выполнения'),
        ),
    ]