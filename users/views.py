from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissons import IsModer, IsUser
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Любой пользователь может зарегистрироваться
        if self.action == "create":
            self.permission_classes = [AllowAny]
        # Пользователь может удалить только себя,
        # и производить методы PUT PATCH RETRIEVE только для своего аккаунта
        elif self.action in ["update", "retrieve", "destroy"]:
            self.permission_classes = [IsUser]
        # Список пользователей доступен только модераторам
        elif self.action == "list":
            self.permission_classes = [IsModer]

        return super().get_permissions()

    def perform_create(self, serializer):
        if serializer.is_valid():
            password = serializer.validated_data.pop("password")
            user = serializer.save()
            user.set_password(password)
            user.save()
