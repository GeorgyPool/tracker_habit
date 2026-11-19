from rest_framework.exceptions import ValidationError


class ValidateTimeForHabit:
    """
    Проверяет что время на выполнение привычки не равно или не меньше времени привычки.
    """

    def __call__(self, attrs):
        time = attrs["time"]
        time_zone = attrs.get("time_zone_habit")

        if time_zone is not None and time_zone <= time:
            raise ValidationError(
                "Время выполнение привычки не может быть меньше или равно времени привычки"
            )


class ValidateReward:
    """Проверят чтобы награду можно было указать только для полезной привычки"""

    def __call__(self, attrs):
        is_nice_habit = attrs["is_nice_habit"]
        reward = attrs.get("reward")

        if reward is not None and is_nice_habit is True:
            raise ValidationError(
                "Для приятной привычки нельзя указать награду, но вы можете указать связанную привычку в дальнейшем"
            )
