from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Аккаунт", on_delete=models.CASCADE, related_name='profile')
    # email = models.EmailField(verbose_name="E-mail", max_length=254)
    phonenumber = models.TextField(verbose_name="Номер телефона", max_length=12, default=None)
    avatar = models.ImageField(verbose_name="Аватар", upload_to="accounts/img", default=None)