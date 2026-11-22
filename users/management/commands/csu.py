from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Создает супер пользователя"

    def handle(self, *args, **options):
        try:
            user = User.objects.create_user(
                email="super@example.com", username="super", tg_id=235680
            )
            user.save()
            user.set_password("098")
            user.save()
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS("Пользователь успешно создан"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Произошла ошибка: {type(e)}"))
