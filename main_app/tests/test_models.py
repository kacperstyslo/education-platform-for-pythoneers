from django.test import TestCase

# Own
from main_app.models import Tasks


class TestTasksTable(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Tasks.objects.create(
            task_id=1,
            task_title="Test Task",
            task_description="This is test task",
            task_starter="def test_task() -> None: pass",
            amount_tests_cases=1,
            task_tests="import pytest\n\nfrom .user_solution import *",
        )

    def setUp(self) -> None:
        self.test_task = Tasks.objects.get(task_id=1)

    def test_task_instance(self) -> None:
        """
        Object self.test_task should be instance of Tasks table.
        """
        self.assertTrue(isinstance(self.test_task, Tasks))

    def test_get_task_id(self) -> None:
        self.assertEqual(self.test_task.task_id, 1, msg="Should be 1")

    def test_task_title_content(self) -> None:
        expected_task_title = "Test Task"
        self.assertEqual(
            self.test_task.task_title, expected_task_title, msg="Should be 'Test Task'"
        )

    def test_task_description_content(self) -> None:
        expected_task_description = "This is test task"
        self.assertEqual(
            self.test_task.task_description,
            expected_task_description,
            msg="Should be 'This is test task'",
        )

    def test_task_starter_content(self) -> None:
        expected_task_starter_content = "def test_task() -> None: pass"
        self.assertEqual(
            self.test_task.task_starter,
            expected_task_starter_content,
            msg="Should be 'def test_task() -> None: pass'",
        )

    def test_default_amount_of_tests_cases(self) -> None:
        self.assertEqual(self.test_task.amount_tests_cases, 1, msg="By default should be 1")

    def test_default_content_of_task_tests(self) -> None:
        expected_task_test_content = "import pytest\n\nfrom .user_solution import *"
        self.assertEqual(
            self.test_task.task_tests,
            expected_task_test_content,
            msg="By default content of task test should be "
            "'import pytest\n\nfrom .user_solution import *'",
        )
