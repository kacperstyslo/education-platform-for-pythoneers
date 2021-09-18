from typing import Dict, List

from django.contrib.auth import get_user_model

# Own
from ranking_app.models import RankingTable
from users_app.models import UsersTasksSolutions


class UsersSolutions:
    """
    This class is created to provide method that get user solutions and user nicknames from two
    different tables. This data is necessary to calculate points for each user.
    """

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def get_from_db() -> List[Dict[str, int]]:
        """
        Caller: ranking_app.services.calculate_users_points.
        This method is created to combine the data from two tables ('User','Users Tasks
        Solutions') together. Data from this two tables is needed to calculate user ranking
        points.
        """
        all_users = list(get_user_model().objects.values("id", "username"))
        users_solutions_data = list(
            UsersTasksSolutions.objects.filter(is_task_passed=True).values(
                "user_nickname", "user_amounts_of_try", "amount_tests_cases_passed"
            )
        )
        for user_solution in users_solutions_data:
            for user in all_users:
                if user["id"] == user_solution["user_nickname"]:
                    user_solution["user_nickname"] = user["username"]
        return users_solutions_data


class UsersPoints:
    """
    This class is created to provides method that save user points into ranking table.
    After saving this points, 'RankingView' view render this points into HTML table.
    """

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def save_into_db(ten_best_users: Dict[str, int]) -> None:
        """
        Caller: ranking_app.calculate_users_points
        This method will save already calculated users points to the 'RankingTable' table.
        """
        RankingTable.objects.all().delete()
        for user_nickname, user_points in ten_best_users.items():
            RankingTable.objects.update_or_create(
                user_nickname=user_nickname, sum_of_all_user_points=user_points
            )
