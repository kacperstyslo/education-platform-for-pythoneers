from typing import Union

from django.http import QueryDict
from django.contrib.auth import get_user_model

# Own
from main_app.models import Tasks
from users_app.models import UsersTasksSolutions
from task_statistics_app.db.models_operators import TaskTries, SuccessfulSubmission


class UsersTasksSolutionsTableUpdater:
    """
    This class provides methods that are used by services (remote_code_execution_app services) to
    update data it the UsersTasksSolutions table.
    """

    def __init__(self, **kwargs: Union[Union[str, int], QueryDict]) -> None:
        self.task_id: int = kwargs["task_id"]
        self.user_id: int = kwargs["user_id"]
        self.task_title: str = kwargs["task_title"]
        self.user_code: str = kwargs["user_code"]
        self.number_of_tests_cases: int = kwargs["number_of_tests_cases"]

    def save_user_solution_into_db(self) -> None:
        """
        Caller: remote_code_execution_app.services.solution_tester.LocalUserSolutionTester

        This method save user solution into database. If solution doesn't exist in database method
        will insert user solution into appropriate field, if solution exist but didn't pass all
        test cases, the method will replace the user's solution with the one already exist in
        the database. If the user solution from the database has passed all test cases, the method
        will not replace the solution from database.
        """

        if not UsersTasksSolutions.objects.filter(
            task_title=self.task_title, user_nickname=self.user_id
        ).exists():
            UsersTasksSolutions.objects.create(
                task_title=self.task_title,
                user_solution=self.user_code,
                user_nickname=get_user_model().objects.get(id=self.user_id),
            )
        elif not UsersTasksSolutions.objects.values_list("is_task_passed", flat=True).get(
            task_title=self.task_title, user_nickname=self.user_id
        ):
            UsersTasksSolutions.objects.filter(
                task_title=self.task_title, user_nickname=self.user_id
            ).update(user_solution=self.user_code)

    def increment_amounts_of_user_try(self) -> int:
        """
        Caller: remote_code_execution_app.services.solution_tester.check_and_convert_tests_output

        This method increment amounts of user try, for chosen task each time if user click 'Check'
        or 'Submit' button except except when the user's solution passes all tests.
        """
        user_amounts_of_try: int = UsersTasksSolutions.objects.values_list(
            "user_amounts_of_try", flat=True
        ).get(task_title=self.task_title, user_nickname=self.user_id)

        if not UsersTasksSolutions.objects.values_list("is_task_passed", flat=True).get(
            task_title=self.task_title, user_nickname=self.user_id
        ):
            TaskTries(self.task_title).increment_by_one()
            UsersTasksSolutions.objects.filter(
                task_title=self.task_title, user_nickname=self.user_id
            ).update(user_amounts_of_try=user_amounts_of_try + 1)

        return user_amounts_of_try

    def update_amount_of_passed_tests_cases(self, amount_of_passed_test_cases: int) -> None:
        """
        Caller: remote_code_execution_app.services.solution_tester.check_and_convert_tests_output

        This method receive number of passed test cases by user code to chosen task, will update
        this amount in appropriate field in DB.
        """
        if not UsersTasksSolutions.objects.values_list("is_task_passed", flat=True).get(
            user_nickname=self.user_id, task_title=self.task_title
        ):
            UsersTasksSolutions.objects.filter(
                task_title=self.task_title, user_nickname=self.user_id
            ).update(amount_tests_cases_passed=amount_of_passed_test_cases)

    def update_user_solution_when_passed_all_tests(self) -> None:
        """
        Caller: remote_code_execution_app.services.solution_tester.check_and_convert_tests_output

        When the user code passes all the prepared tests for the task this method will change field
        'is_task_passed' value from False to True.
        """
        UsersTasksSolutions.objects.filter(
            task_title=self.task_title, user_nickname=self.user_id
        ).update(is_task_passed=True, user_solution=self.user_code)

        SuccessfulSubmission(self.task_title).increment_by_one()


class TasksTableUpdater(UsersTasksSolutionsTableUpdater):
    """
    This class provides methods that are used by service (remote_code_execution_app services) to
    update data it the Tasks table.
    """

    def update_amount_of_tests_case(self) -> None:
        """
        Caller: remote_code_execution_app.services.solution_tester.LocalUserSolutionTester

        Every time the user has not passed all the tests to chosen task and clicks 'Submit' or
        'Check' button this method will increment field 'amount test_cases' by one.
        """
        if (
            Tasks.objects.values_list("amount_tests_cases", flat=True).get(task_id=self.task_id)
            != self.number_of_tests_cases
        ):
            Tasks.objects.filter(task_id=self.task_id).update(
                amount_tests_cases=self.number_of_tests_cases
            )
