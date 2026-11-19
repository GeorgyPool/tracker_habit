from django.shortcuts import render
from rest_framework import viewsets

from tracker.models import AssociatedHabit, Habit
from tracker.serializers import AssociatedHabitSerializer, HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class AssociatedHabitViewSet(viewsets.ModelViewSet):
    queryset = AssociatedHabit.objects.all()
    serializer_class = AssociatedHabitSerializer
