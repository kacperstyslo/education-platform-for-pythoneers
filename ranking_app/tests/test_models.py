from django.test import TestCase

# Own
from ranking_app.models import RankingTable


class TestTasksTable(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        RankingTable.objects.create(user_nickname="Test User", sum_of_all_user_points=0)

    def setUp(self) -> None:
        self.test_ranking = RankingTable.objects.get(id=1)

    def test_ranking_instance(self) -> None:
        """
        Object self.test_ranking should be instance of RankingTable table.
        """
        self.assertTrue(isinstance(self.test_ranking, RankingTable))

    def test_get_ranking_id(self) -> None:
        self.assertEqual(self.test_ranking.id, 1, msg="Should be 1")

    def test_user_nickname_content(self) -> None:
        expected_user_nickname = "Test User"
        self.assertEqual(
            self.test_ranking.user_nickname, expected_user_nickname, msg="Should be 'Test User'"
        )

    def test_user_nickname_max_length(self) -> None:
        expected_user_nickname_max_length = 50
        actual_user_nickname_max_length = self.test_ranking._meta.get_field(
            "user_nickname"
        ).max_length
        self.assertEqual(
            actual_user_nickname_max_length, expected_user_nickname_max_length, msg="Should be 50"
        )

    def test_default_value_of_sum_of_all_user_points_field(self) -> None:
        expected_default_value = 0
        self.assertEqual(
            self.test_ranking.sum_of_all_user_points, expected_default_value, msg="Should be 0"
        )
