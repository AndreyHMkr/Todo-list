from django.contrib import admin

from catalog import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "deadline", "task_is_done",)
