from django.urls import path
from rest_framework.routers import DefaultRouter

from tracker.apps import TrackerConfig

from . import views

app_name = TrackerConfig.name

router = DefaultRouter()
router.register(r"habit", views.HabitViewSet, basename="habit")
router.register(r"associated_habit", views.AssociatedHabitViewSet, basename="associated_habit")

urlpatterns = [path("public/", views.PublicHabit.as_view(), name="public")] + router.urls
