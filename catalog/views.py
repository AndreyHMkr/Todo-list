from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from catalog.forms import TaskForm
from catalog.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "home.html"

    def get_queryset(self):
        return Task.objects.all().order_by("task_is_done", "-created_at")


class Tags(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags_list.html"


class TagAdd(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tag_form.html"
    success_url = reverse_lazy("tags")


class TagUpdate(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags")
    template_name = "tag_form.html"


class TagDelete(generic.DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("tags")


class TaskAdd(generic.CreateView):
    form_class = TaskForm
    template_name = "add_task.html"
    success_url = reverse_lazy("home")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_update.html"
    success_url = reverse_lazy("home")


def toggle_task_status(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.task_is_done = not task.task_is_done
    task.save()
    return redirect("home")


class TaskDelete(generic.DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("home")
