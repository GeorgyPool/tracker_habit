from datetime import datetime, timedelta

import requests
from django.utils import timezone

from config.settings import URL_BOT
from tracker.models import AssociatedHabit, Habit


def get_habit_list(user):
    return Habit.objects.filter(owner=user)


def get_associated_habit_list(user):
    return AssociatedHabit.objects.filter(owner=user)


def manager_sends_habit_every_day() -> None:
    """Отправляет ежедневные напоминания о привычках в Telegram.
    Функция находит привычки с периодичностью «каждый день», время которых совпадает с текущим,
    формирует сообщение с деталями привычки и отправляет его владельцу через Telegram API.
    """

    current_time = timezone.localtime().replace(second=0, microsecond=0).time()
    habits = Habit.objects.filter(periodic_habit=Habit.every_days, time=current_time)

    for habit in habits:
        reward_part = f"\nНаграда: {habit.reward}" if habit.reward else ""
        assoc = ""
        if AssociatedHabit.objects.filter(owner=habit.owner, habit=habit).exists():
            assoc += f"\nПриятная привычка: {habit.associated_habit.do}"

        message = f"Время для привычки: {habit.do}{reward_part}{assoc}"
        params = {"chat_id": habit.owner.tg_id, "text": message}
        requests.get(url=URL_BOT, params=params)


def manager_sends_habit_every_tree_days() -> None:
    """Отправляет напоминания о привычках, которые должны приходить каждые три дня.
    Функция проверяет привычки с периодичностью «каждые 3 дня», у которых:
    - дата последней проверки — ровно 3 дня назад,
    - время совпадает с текущим.
    Для каждой подходящей привычки обновляет date_check на сегодня и отправляет сообщение в Telegram.
    """

    day = timezone.now().date() - timedelta(days=3)
    current_time = timezone.localtime().replace(second=0, microsecond=0).time()

    for habit in Habit.objects.filter(
        periodic_habit=Habit.every_three_days, date_check=day, time=current_time
    ):
        habit.date_check = timezone.now().date()
        habit.save()
        reward_part = f"\nНаграда: {habit.reward}" if habit.reward else ""
        assoc = ""
        if AssociatedHabit.objects.filter(owner=habit.owner, habit=habit).exists():
            assoc += f"\nПриятная привычка: {habit.associated_habit.do}"

        message = f"Время для привычки: {habit.do}{reward_part}{assoc}"
        params = {"chat_id": habit.owner.tg_id, "text": message}
        requests.get(url=URL_BOT, params=params)


def manager_sends_habit_every_week() -> None:
    """Отправляет напоминания о привычках, которые должны приходить каждые три дня.
    Функция проверяет привычки с периодичностью «каждые 7 дня», у которых:
    - дата последней проверки — ровно 7 дней назад,
    - время совпадает с текущим.
    Для каждой подходящей привычки обновляет date_check на сегодня и отправляет сообщение в Telegram.
    """

    day = timezone.now().date() - timedelta(days=3)
    current_time = timezone.localtime().replace(second=0, microsecond=0).time()

    for habit in Habit.objects.filter(
        periodic_habit=Habit.every_weeks, date_check=day, time=current_time
    ):
        habit.date_check = timezone.now().date()
        habit.save()
        reward_part = f"\nНаграда: {habit.reward}" if habit.reward else ""
        assoc = ""
        if AssociatedHabit.objects.filter(owner=habit.owner, habit=habit).exists():
            assoc += f"\nПриятная привычка: {habit.associated_habit.do}"

        message = f"Время для привычки: {habit.do}{reward_part}{assoc}"
        params = {"chat_id": habit.owner.tg_id, "text": message}
        requests.get(url=URL_BOT, params=params)
