from django.test import TestCase

# Own
from task_statistics_app.models import TasksStatistics


class TestTasksStatistics(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        TasksStatistics.objects.create(
            task_title="Test Task",
            sum_of_all_tries_per_task=0,
            sum_of_all_successful_submission_per_task=0,
        )

    def setUp(self) -> None:
        self.test_task_statistics = TasksStatistics.objects.get(task_id=1)

    def test_task_statistics_instance(self) -> None:
        """
        Object self.test_task_statistics should be instance of TasksStatistics table.
        """
        self.assertTrue(isinstance(self.test_task_statistics, TasksStatistics))

    def test_get_task_statistics_id(self) -> None:
        self.assertEqual(self.test_task_statistics.id, 1, msg="Should be 1")

    def test_task_statistics_title_content(self) -> None:
        expected_task_statistics_title = "Test Task"
        self.assertEqual(
            self.test_task_statistics.task_title,
            expected_task_statistics_title,
            msg="Should be 'Test Task'",
        )

    def test_default_amount_of_sum_of_all_tries_per_task(self) -> None:
        self.assertEqual(
            self.test_task_statistics.sum_of_all_tries_per_task, 0, msg="By default " "should be 0"
        )

    def test_default_amount_of_sum_of_all_successful_submission_per_task(self) -> None:
        self.assertEqual(
            self.test_task_statistics.sum_of_all_successful_submission_per_task,
            0,
            msg="By default " "should be 0",
        )
