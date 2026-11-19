from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import check_phone_number


class User(AbstractUser):
    """
    Переопределение класса AbstractUser.
    """

    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    phone_number = models.CharField(
        max_length=11,
        verbose_name="Номер телефона",
        unique=True,
        blank=True,
        null=True,
        validators=[check_phone_number],
    )

    tg_id = models.IntegerField(unique=True, verbose_name="Телеграм id")

    avatar = models.ImageField(
        upload_to="avatar/", verbose_name="Аватарка", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["created_at", "email"]
