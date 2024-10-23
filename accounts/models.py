from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    surname = models.CharField(max_length=150, blank=True, null=True, verbose_name="Фамилия")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Фото")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Страна")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
    def __str__(self):
        return self.email