from rest_framework import serializers

from tracker import models, validators


class AssociatedHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssociatedHabit
        exclude = ["created_at"]
        extra_kwargs = {"created_at": {"read_only": True}}


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Habit
        exclude = ["created_at"]
        validators = [
            validators.ValidateTimeForHabit(),
            validators.ValidateReward(),
        ]
        extra_kwargs = {"created_at": {"read_only": True}}
