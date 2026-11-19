from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "phone_number", "tg_id"]
        extra_kwargs = {"password": {"write_only": True}}
