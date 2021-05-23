from django.db import models

from accounts.forms import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Аккаунт", on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="E-mail", max_length=254)
    phonenumber = models.TextField(verbose_name="Номер телефона", max_length=12)