from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig

from . import views

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"options", views.UserViewSet, basename="options")

urlpatterns = [] + router.urls
