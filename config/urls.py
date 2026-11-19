from django.contrib import admin
from django.urls import include, path

from tracker.apps import TrackerConfig
from users.apps import UsersConfig

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace=UsersConfig.name)),
    path("tracker/", include("tracker.urls", namespace=TrackerConfig.name)),
]
