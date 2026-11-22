from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.models import AssociatedHabit, Habit
from tracker.paginations import PaginationTracker
from tracker.permissions import IsOwner
from tracker.serializers import AssociatedHabitSerializer, HabitSerializer
from tracker.services import get_associated_habit_list, get_habit_list
from users.permissons import IsModer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = PaginationTracker

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["destroy", "update"]:
            self.permission_classes = [IsOwner]
        elif self.action == "retrieve":
            self.permission_classes = [IsOwner, IsModer]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Переопределяет метод получения list чтобы пользователи могли видеть только свои привычки,
        а модераторы могли видеть список всех привычек
        """
        if not self.request.user.groups.filter(name="moderators").exists():
            # вызывает функцию из tracker/service.py для получения
            # всех связанных привычек для конкретного пользователя
            habit_user = get_habit_list(user=self.request.user)
            self.queryset = habit_user

        return super().list(request, *args, **kwargs)


class AssociatedHabitViewSet(viewsets.ModelViewSet):
    queryset = AssociatedHabit.objects.all()
    serializer_class = AssociatedHabitSerializer
    pagination_class = PaginationTracker

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["destroy", "update"]:
            self.permission_classes = [IsOwner]
        elif self.action == "retrieve":
            self.permission_classes = [IsModer, IsOwner]

        return super().get_permissions()

    def perform_create(self, serializer):
        habit = serializer.validated_data["habit"]
        user = self.request.user

        if AssociatedHabit.objects.filter(owner=user.pk, habit=habit.pk).exists():
            raise ValidationError("Связанная привычка уже добавлена")

        elif habit.owner == user:
            serializer.save(owner=user)

        else:
            raise ValidationError("Только владелец может добавить связанную привычку")

    def list(self, request, *args, **kwargs):
        """
        Переопределяет метод получения list чтобы пользователи могли видеть только свои связанные привычки,
        а модераторы могли видеть список всех cвязанных привычек
        """
        if not self.request.user.groups.filter(name="moderators").exists():
            # вызывает функцию из tracker/service.py для получения
            # всех связанных привычек для конкретного пользователя
            associated_habit = get_associated_habit_list(user=self.request.user)
            self.queryset = associated_habit

        return super().list(request, *args, **kwargs)


class PublicHabit(APIView):
    """
    Представление для публичных привычек
    """

    def get(self, request, *args, **kwargs):
        habits = Habit.objects.filter(is_public=True)
        paginator = PaginationTracker()
        paginator.paginate_queryset(habits, request, view=self)
        serializer = HabitSerializer(habits, many=True)

        return paginator.get_paginated_response(serializer.data)
