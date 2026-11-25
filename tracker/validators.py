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
                raise ValidationError("Время выполнения привычки не может превышать 120 сек")


class ValidateAddAssociatedHabit:
    """
    Проверяет что связанную привычку можно добавить только к привычке у которой отсутствует награда
    """

    def __call__(self, attrs):

        habit = attrs["habit"]

        if habit.reward is not None:
            raise ValidationError(
                "Связанную приятную привычку можно добавить "
                "только к полезной привычке у которой отсутствует награда за привычку"
            )
