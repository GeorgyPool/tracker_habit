from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from django.db import IntegrityError

from users.models import User


class Command(BaseCommand):
    help = "Создает пользователя с правами модератора"

    def handle(self, *args, **options):

        try:
            Group.objects.create(name="moderators")
            self.stdout.write(self.style.SUCCESS("Группа модераторов успешно создана"))
        except IntegrityError as e:
            self.stdout.write(self.style.WARNING(f"Группа уже создана: {e}"))

        try:
            user = User.objects.create(email="moder_user@example.com", tg_id=2345678)
            user.set_password("moder123")
            user.save()
            self.stdout.write(self.style.SUCCESS("Пользователь создан"))
        except IntegrityError as e:
            self.stdout.write(self.style.WARNING(f"Такой пользователь уже существует: {e}"))

        try:
            get_group = Group.objects.get(name="moderators")
            user = User.objects.get(email="moder_user@example.com")
            user.groups.add(get_group)
            self.stdout.write(self.style.SUCCESS("Пользователь с правами модератора успешно создан"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Произошла ошибка: {type(e)}"))
