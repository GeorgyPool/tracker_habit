import re

from django.core.exceptions import ValidationError


def check_phone_number(phone_number: str):
    """
    Проверяет корректность введенного телефонного номера
    для модели User.
    """
    if not re.fullmatch(r"[78]\d{10}", phone_number):
        raise ValidationError("Номер должен начинаться с 8 или 7 и содержать 11 цифр")
