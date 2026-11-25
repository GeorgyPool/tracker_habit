from rest_framework import serializers

from tracker import models, validators


class AssociatedHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AssociatedHabit
        exclude = ["created_at"]
        validators = [validators.ValidateAddAssociatedHabit()]
        extra_kwargs = {"created_at": {"read_only": True}}


class HabitSerializer(serializers.ModelSerializer):

    associated_habit = AssociatedHabitSerializer(many=True, read_only=True)

    class Meta:
        model = models.Habit
        exclude = ["created_at"]
        validators = [validators.ValidateTimeForHabit()]
        extra_kwargs = {"created_at": {"read_only": True}}
