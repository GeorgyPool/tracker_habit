import requests
from celery import shared_task

from config.settings import URL_BOT
from tracker.models import AssociatedHabit, Habit
from tracker.services import (manager_sends_habit_every_day,
                              manager_sends_habit_every_tree_days,
                              manager_sends_habit_every_week)


@shared_task()
def send_habit():
    manager_sends_habit_every_day()
    manager_sends_habit_every_tree_days()
    manager_sends_habit_every_week()

    # for habit in Habit.objects.filter(periodic_habit=Habit.every_days):
    #     reward = f"\nНаграда: {habit.reward}" if habit.reward is not None else ""
    #     asec = ""
    #     if AssociatedHabit.objects.filter(owner=habit.owner, habit=habit).exists():
    #         asec += f"\n{habit.associated_habit.do}"
    #     message = f"Время для привычки: {habit.do}{reward}{asec}"
    #     params = {"chat_id": habit.owner.tg_id, "text": message}
    #     requests.get(url=URL_BOT, params=params)
