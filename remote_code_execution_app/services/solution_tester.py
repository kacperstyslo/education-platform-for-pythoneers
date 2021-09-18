# pylint: disable=R1732

import subprocess
from typing import Dict, Union

from django.http import QueryDict

# Own
# DB operators
from remote_code_execution_app.db.services_operator import (
    UsersTasksSolutionsTableUpdater,
    TasksTableUpdater,
)


class LocalUserSolutionTester:
    """
    This class provides all the methods that check the user's solution.
    The methods in this class run test cases for the user code ('to check if the code submitted by
    the user fully solves the task'). Also methods in this class convert tests cases output to
    more manageable data type form.
    """

    def __init__(self, **kwargs) -> None:
        self.task_id: int = kwargs["task_id"]
        self.user_id: int = kwargs["user_id"]
        self.task_title: str = kwargs["task_title"]
        self.user_code: QueryDict = kwargs["user_code"]
        self.number_of_tests_cases: int = kwargs["number_of_tests_cases"]
        self.tasks_tests_marks: Dict[int, str] = {
            1: "fib_test_case",
            2: "palindrome_test_case",
        }
        self._raw_tests_cases_output: Dict[str, Union[int, bool]] = {
            "amount_of_test_cases": self.number_of_tests_cases,
            "amount_of_passed_test_cases": 0,
            "user_amounts_of_try": 1,
        }
        self.db_user_task_solutions_updater = UsersTasksSolutionsTableUpdater(
            task_id=self.task_id,
            user_id=self.user_id,
            task_title=self.task_title,
            user_code=self.user_code,
            number_of_tests_cases=self.number_of_tests_cases,
        )
        self.db_tasks_updater = TasksTableUpdater(**kwargs)

    def __call__(self) -> Dict[str, Union[int, bool]]:
        self.db_user_task_solutions_updater.save_user_solution_into_db()
        self.db_tasks_updater.update_amount_of_tests_case()
        raw_test_case_output = self.run_tests()
        self.__check_and_convert_tests_output(raw_test_case_output)
        return self.__return_converted_data()

    def run_tests(self) -> subprocess.Popen:
        """
        This method execute tests for 'user task solution' locally using the Pytest module. After
        executing this tests method will return raw test case output.
        """
        return subprocess.Popen(
            [
                "pytest",
                "-m",
                "test_user_solution.py",
                "-m",
                f"{self.tasks_tests_marks.get(self.task_id)}",
                "--tb=line",
                "--no-summary",
                "--no-header",
                "-q",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

    def __check_and_convert_tests_output(self, tests_output: subprocess.Popen) -> None:
        """
        This function receive raw test cases output (after testing the user code by run_test
        function). After receive data,method will convert this data.
        """
        stdout, _ = tests_output.communicate()
        stdout = stdout.decode("UTF-8")

        self.__count_number_of_passed_tests(stdout)

        self.db_user_task_solutions_updater.update_amount_of_passed_tests_cases(
            self._raw_tests_cases_output.get("amount_of_passed_test_cases")
        )

        if all(self._raw_tests_cases_output.values()):
            self._raw_tests_cases_output["all_tests_passed"] = True
            self.db_user_task_solutions_updater.update_user_solution_when_passed_all_tests()

        self._raw_tests_cases_output[
            "user_amounts_of_try"
        ] = self.db_user_task_solutions_updater.increment_amounts_of_user_try()

    def __count_number_of_passed_tests(self, stdout: str) -> None:
        """
        This method count the number of passed test cases by 'user solution'.
        """
        for test_number, test_case in enumerate(stdout[0 : self.number_of_tests_cases], 1):
            if test_case == ".":
                self._raw_tests_cases_output[f"test_case_{test_number}"] = True
                self._raw_tests_cases_output["amount_of_passed_test_cases"] += 1
            elif test_case == "F":
                self._raw_tests_cases_output[f"test_case_{test_number}"] = False

    def __return_converted_data(self) -> Dict[str, Union[int, bool]]:
        """
        When this method is called, test case output is already converted.
        Method only return converted tests case output to send_converted_tests_cases_output view.
        """
        return self._raw_tests_cases_output
