from django.db import models
from django.contrib.auth import get_user_model

# Own
from main_app.models import Tasks


class UsersTasksSolutions(models.Model):
    """
    This table stores users solutions.
    """

    class Meta:
        ordering = ("-amount_tests_cases_passed", "user_amounts_of_try")

    task_title = models.ForeignKey(to=Tasks, on_delete=models.SET_NULL, null=True)
    user_nickname = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
    user_solution = models.TextField(blank=True)
    user_amounts_of_try = models.IntegerField(default=1)
    amount_tests_cases_passed = models.IntegerField(default=0)
    is_task_passed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"User: {self.user_nickname} Task: {self.task_title}  Passed: {self.is_task_passed}"

    def get_excerpt_user_solution(self, number_of_characters: int) -> str:
        return self.user_solution[:number_of_characters]
