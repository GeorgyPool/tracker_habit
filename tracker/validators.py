import datetime

from rest_framework.exceptions import ValidationError


class ValidateTimeForHabit:
    """
    Проверяет чтобы время на выполнение привычки не превышало 120 секунд.
    """

    def __call__(self, attrs):

        time_zone_habit = attrs.get("time_zone_habit")
        string_time = "00:02:00"
        seconds = datetime.datetime.strptime(string_time, "%H:%M:%S").time()

        if time_zone_habit is not None:
            if time_zone_habit > seconds:
                raise ValidationError(
                    "Время выполнения привычки не может превышать 120 сек"
                )
