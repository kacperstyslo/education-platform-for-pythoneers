from django.test import TestCase
from django.contrib.auth import get_user_model

# Own
from main_app.models import Tasks
from users_app.models import UsersTasksSolutions


class TestUsersTasksSolutions(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        UsersTasksSolutions.objects.create(
            task_title=Tasks.objects.create(task_title="Test Task"),
            user_nickname=get_user_model().objects.create(username="test_user"),
            user_solution="def test_task(): pass",
            user_amounts_of_try=1,
            amount_tests_cases_passed=0,
            is_task_passed=False,
        )

    def setUp(self) -> None:
        self.test_users_tasks_solutions = UsersTasksSolutions.objects.get(id=1)

    def test_users_tasks_solutions_instance(self) -> None:
        """
        Object self.test_users_tasks_solutions should be instance of UsersTasksSolutions table.
        """
        self.assertTrue(isinstance(self.test_users_tasks_solutions, UsersTasksSolutions))

    def test_get_users_tasks_solutions_id(self) -> None:
        self.assertEqual(self.test_users_tasks_solutions.id, 1, msg="Should be 1")

    def test_users_tasks_solutions_task_title_content(self) -> None:
        expected_task_title = "Test Task"
        self.assertEqual(
            Tasks.objects.values_list("task_title", flat=True)[0],
            expected_task_title,
            msg="Should be 'Test Task'",
        )

    def test_users_tasks_solutions_user_nickname_content(self) -> None:
        expected_user_nickname = "test_user"
        self.assertEqual(
            get_user_model().objects.values_list("username", flat=True)[0],
            expected_user_nickname,
            msg="Should be 'test_user'",
        )

    def test_users_tasks_solutions_user_solution_content(self) -> None:
        expected_user_solution = "def test_task(): pass"
        self.assertEqual(
            self.test_users_tasks_solutions.user_solution,
            expected_user_solution,
            msg="Should be 'def test_task(): pass'",
        )

    def test_default_value_of_field_user_amounts_of_try(self) -> None:
        self.assertEqual(
            self.test_users_tasks_solutions.user_amounts_of_try, 1, msg="By default " "should be 1"
        )

    def test_default_value_of_field_amount_tests_cases_passed(self) -> None:
        self.assertEqual(
            self.test_users_tasks_solutions.amount_tests_cases_passed,
            0,
            msg="By default " "should be 0",
        )

    def test_default_value_of_field_is_task_passed(self) -> None:
        self.assertFalse(
            self.test_users_tasks_solutions.is_task_passed,
            msg="By default should be False",
        )
