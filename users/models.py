from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Телефон", help_text="Введите номер телефона")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон", help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Аватар",)
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name="Страна", help_text="Укажите Вашу страну")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
