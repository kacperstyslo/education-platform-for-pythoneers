from django.db import models


class Tasks(models.Model):
    """
    This table store all tasks data but without users solutions.
    """

    class LevelOfTaskDifficulty(models.TextChoices):
        """
        This class store all difficulty levels for tasks.
        """

        EASY = "Easy", "A beginner would be able to solve this task"
        MEDIUM = "Medium", "Intermediate would be able to solve this task"
        HARD = "Hard", "Only real Pythoneer would be able to solve this task"

    class Meta:
        ordering = ["pk"]

    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=30)
    task_description = models.TextField()
    task_starter = models.TextField()
    level_of_task_difficulty = models.CharField(
        max_length=10, choices=LevelOfTaskDifficulty.choices, default="Easy"
    )
    amount_tests_cases = models.IntegerField(default=1)
    task_tests = models.TextField(default="import pytest\n\nfrom .user_solution import *")

    def __str__(self) -> str:
        return str(self.task_title)
