from datetime import datetime

import requests
from celery import shared_task

from config.settings import API_BOT
from tracker.models import Habit


@shared_task()
def send_habit():
    now = datetime.now()
    d_now = datetime.strftime(now, "%H:%M")
    time = datetime.strptime(d_now, "%H:%M").time()
    habit = Habit.objects.filter(time=time)

    if habit.exists():
        for hab in habit:
            data = {"chat_id": hab.owner.tg_id, "text": hab.do}
            response = requests.post(
                url=f"https://api.telegram.org/bot{API_BOT}/sendMessage", data=data
            )
