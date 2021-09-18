# Own
from task_statistics_app.models import TasksStatistics
from users_app.models import UsersTasksSolutions


class TaskTries:
    """
    This class has methods that provide the ability to get/update values from 'TasksStatistics'
    table.
    """

    def __str__(self) -> str:
        return self.__class__.__name__

    def __init__(self, task_title: str) -> None:
        self.task_title: str = task_title
        self.num_per_task: int = TasksStatistics.objects.values_list(
            "sum_of_all_tries_per_task", flat=True
        ).get(task_title=task_title)

    def increment_by_one(self) -> None:
        """
        DB_Operator: remote_code_execution_app.db services_operator

        Every time if the user's solution does not pass all test cases for given task, this method
        will increment number of tries in 'Tasks Statistics' table for right task by one.
        """
        TasksStatistics.objects.filter(task_title=self.task_title).update(
            sum_of_all_tries_per_task=self.num_per_task + 1
        )


class SuccessfulSubmission:
    __doc__ = TaskTries.__doc__

    def __init__(self, task_title: str) -> None:
        self.task_title: str = task_title
        self.num_per_task = UsersTasksSolutions.objects.filter(
            task_title=self.task_title, is_task_passed=True
        ).count()

    def increment_by_one(self) -> None:
        """
        Caller:
        remote_code_execution_app.db.services_operator.update_user_solution_when_passed_all_tests

        Every time if the user's solution does pass all test cases for given task, this method will
        increment number of successful submissions in 'Tasks Statistics' table for right task.
        """
        TasksStatistics.objects.filter(task_title=self.task_title).update(
            sum_of_all_successful_submission_per_task=self.num_per_task + 1
        )

    def get_all(self) -> int:
        """
        Caller: task_statistics.services.task_statistics_calculator.calc_task_success_rate &
                remote_code_execution_app.views.CodeEditorView

        This method will get number of successful submissions for chosen task from
        'Tasks Statistics' table.
        """
        return self.num_per_task
