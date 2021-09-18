import heapq
from typing import Dict, List, Union

# Own
# DB operator
from ranking_app.db.services_operator import UsersPoints, UsersSolutions


class UsersPointsCalculator:
    """
    This class provides all methods to calculate user points.
    """

    def __init__(self) -> None:
        self.ten_best_users: Dict[str, int] = {}
        self.users_solutions_unconverted = UsersSolutions().get_from_db()
        self.users_solutions_converted: Dict[Union[str, int], int] = {
            user_nickname.get("user_nickname"): 0
            for user_nickname in self.users_solutions_unconverted
        }

    def __call__(self) -> None:
        self.__convert_solutions_from_database()
        self.__get_ten_users_with_highest_number_of_points()
        UsersPoints().save_into_db(self.ten_best_users)

    def __convert_solutions_from_database(self) -> None:
        """
        This method will convert users solutions from database to Dict type.
        """
        for user_points in self.users_solutions_unconverted:
            self.users_solutions_converted[
                user_points.get("user_nickname")
            ] += self.calc_points_per_task(
                user_amounts_of_try=user_points.get("user_amounts_of_try"),
                amount_tests_cases_passed=user_points.get("amount_tests_cases_passed"),
            )

    def __get_ten_users_with_highest_number_of_points(self) -> None:
        """
        This method will get the nicknames of the ten users with the most points. After
        collecting the nicknames, the method will get the points of these users and combine
        nicknames and points together into self.ten_best_users dictionary (nickname: points).
        """
        ten_best_users_nicknames: List[str] = heapq.nlargest(
            10, self.users_solutions_converted, key=self.users_solutions_converted.get
        )
        for nickname in ten_best_users_nicknames:
            self.ten_best_users[nickname] = self.users_solutions_converted.get(nickname)

    @staticmethod
    def calc_points_per_task(user_amounts_of_try: int, amount_tests_cases_passed: int) -> int:
        """
        When while calculating points (amount_tests_cases_passed - user_amounts_of_try) result
        will be more than 0 then return calculated points * 100 else return only 100 (because
        task was completed but user try to complete task to much times).
        """
        user_points: int = amount_tests_cases_passed - user_amounts_of_try
        return user_points * 100 if user_points > 0 else 100
