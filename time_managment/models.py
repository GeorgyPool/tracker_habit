from django.db import models

from tracker.models import Habit
from users.models import User


class TimeManagement(models.Model):

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="time_management",
        verbose_name="Получатель",
        blank=True,
        null=True,
    )

    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="time_management",
        blank=True,
        null=True,
    )

    date = models.DateTimeField(verbose_name="Время отправления", blank=True, null=True)

    def __str__(self):
        return f"Пользователь: {self.recipient}, привычка: {self.habit}"

    class Meta:
        verbose_name = "Учет времени"
        verbose_name_plural = "Учет времени"
        ordering = ["-date"]
