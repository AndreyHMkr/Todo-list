from django.urls import path
from catalog.views import (
    TaskAdd,
    IndexView,
    toggle_task_status,
    TaskDelete,
    TaskUpdate,
    Tags,
    TagAdd,
    TagUpdate,
    TagDelete
)

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("tags", Tags.as_view(), name="tags"),
    path("tag/create", TagAdd.as_view(), name="tag-add"),
    path("tag/<int:pk>/update", TagUpdate.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDelete.as_view(), name="tag-delete"),
    path("add_task", TaskAdd.as_view(), name="add-task"),
    path("toggle-task/<int:pk>/", toggle_task_status, name="toggle-task"),
    path("task/<int:pk>/delete", TaskDelete.as_view(), name="task-delete"),
    path("task/<int:pk>/update", TaskUpdate.as_view(), name="task-update"),

]
