from django.db import models

# Own
from main_app.models import Tasks


class TasksStatistics(models.Model):
    """
    This table store all statistic about tasks.
    """

    class Meta:
        ordering = (
            "-sum_of_all_tries_per_task",
            "sum_of_all_successful_submission_per_task",
        )

    task_title = models.OneToOneField(Tasks, on_delete=models.SET_NULL, null=True)
    sum_of_all_tries_per_task = models.IntegerField(default=0)
    sum_of_all_successful_submission_per_task = models.IntegerField(default=0)
