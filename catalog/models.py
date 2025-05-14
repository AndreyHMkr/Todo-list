from django.db import models

class Task(models.Model):
    content = models.TextField(verbose_name="Task Description")
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    deadline = models.DateTimeField(blank=True, null=True, verbose_name="Deadline")
    task_is_done = models.BooleanField(default=False, verbose_name="Task is Done")
    tags = models.ManyToManyField("Tag", related_name="tasks", verbose_name="Tags")


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
