from django.db import models

from users.models import User


class Habit(models.Model):
    """Модель привычки."""

    every_days = "Каждый день"
    every_three_days = "Каждые три дня"
    every_weeks = "Каждую неделю"

    PERIODIC_HUBIT_CHOICES = [
        (every_days, "Каждый день"),
        (every_three_days, "Каждые три дня"),
        (every_weeks, "Каждую неделю"),
    ]

    owner = models.ForeignKey(
        User,
        related_name="user_habit",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )

    do = models.CharField(verbose_name="Действие", max_length=100)

    time = models.TimeField(verbose_name="Время выполнения")

    time_zone_habit = models.TimeField(verbose_name="Время на выполнение привычки", blank=True, null=True)

    periodic_habit = models.CharField(
        verbose_name="Периодичность выполнения",
        choices=PERIODIC_HUBIT_CHOICES,
        default=every_days,
        max_length=20,
    )

    place = models.CharField(verbose_name="Место выполнения", max_length=100, null=True, blank=True)

    reward = models.CharField(verbose_name="Вознаграждение", max_length=100, blank=True, null=True)

    is_public = models.BooleanField(verbose_name="Доступна для просмотра другим", default=False)

    date_check = models.DateField(verbose_name="Дата проверки для отправки", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return f"Пользователь : {self.owner}, Привычка: {self.do}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["created_at"]


class AssociatedHabit(models.Model):
    """Связанная привычка для приятной привычки"""

    owner = models.ForeignKey(
        User,
        related_name="associated_habit_user",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )

    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="associated_habit",
        verbose_name="Связанная привычка",
    )

    do = models.CharField(verbose_name="Приятная привычка", max_length=100)

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return f"Пользователь :{self.owner}, Привычка :{self.do}"

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"
        ordering = ["created_at"]
