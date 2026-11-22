from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from tracker.models import AssociatedHabit, Habit
from tracker.permissions import IsOwner
from tracker.serializers import AssociatedHabitSerializer, HabitSerializer
from users.permissons import IsModer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["destroy", "retrieve", "update"]:
            self.permission_classes = [IsOwner]
        elif self.action == "list":
            self.permission_classes = [IsModer]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AssociatedHabitViewSet(viewsets.ModelViewSet):
    queryset = AssociatedHabit.objects.all()
    serializer_class = AssociatedHabitSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["destroy", "update"]:
            self.permission_classes = [IsOwner]
        elif self.action == "list":
            self.permission_classes = [IsModer]
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
