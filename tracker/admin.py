from django.contrib import admin

from tracker import models


@admin.register(models.Habit)
class AdminHabit(admin.ModelAdmin):
    list_display = ("id", "owner", "do")
    list_filter = ("created_at", "id")
