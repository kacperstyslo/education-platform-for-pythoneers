# pylint: disable=C0413
from os import path
from inspect import cleandoc

import django

django.setup()

from django.contrib.auth import get_user_model

# Own
from main_app.models import Tasks
from task_statistics_app.models import TasksStatistics


def create_super_user() -> None:
    """
    This method was created to able tests run locally on Docker.
    """
    User = get_user_model()
    if not User.objects.filter(username="root").exists():
        User.objects.create_superuser("root", "root@gmail.com", "toor123456")


def create_tasks() -> None:
    """
    This method was created to able tests run locally on Docker.
    """
    if not Tasks.objects.filter(task_title="Nth Fibonacci Sequence"):
        Tasks.objects.create(
            task_title="Nth Fibonacci Sequence",
            task_description="Write a function that takes in an "
            "integer (n) and returns the nth "
            "Fibonacci number.",
            task_starter="def nth_fib(n: int) -> int:\n\tpass",
            task_tests=cleandoc(
                '''
    import pytest
    from .user_solution import *
    
    @pytest.mark.fib_test_case
    def test_fib_first():
        """
        Test for fib when n = 2
        """
        assert 1 == nth_fib(2)
        
    @pytest.mark.fib_test_case
    def test_fib_second():
        """
        Test for fib when n = 6
        """
        assert 8 == nth_fib(6)
    
    @pytest.mark.fib_test_case
    def test_fib_third():
        """
        Test for fib when n = 19
        """
        assert 4181 == nth_fib(19)
            ''',
            ),
        )
        TasksStatistics.objects.create(
            task_title=Tasks.objects.get(task_title="Nth Fibonacci Sequence"),
            sum_of_all_tries_per_task=0,
            sum_of_all_successful_submission_per_task=0,
        )

    if not Tasks.objects.filter(task_title="Palindrome Checker"):
        Tasks.objects.create(
            task_title="Palindrome Checker",
            task_description="Write a function that takes in a non-empty string and that returns a "
            "boolean representing "
            "whether the string is palindrome.",
            task_starter="def palindrome(string: str) -> bool:\n\tpass",
            task_tests=cleandoc(
                '''
    import pytest
    from .user_solution import *
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_first():
        """
        Palindrome('abcdcba') should return true.
        """
        assert palindrome('abcdcba') is True
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_second():
        """
        Palindrome('nope') should return true.
        """
        assert palindrome('nope') is False
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_third():
        """
        Palindrome('aaaaaaaaaa') should return true.
        """
        assert palindrome('aaaaaaaaaa') is True
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_fourth():
        """
        Palindrome('not a palindrome') should return false.
        """
        assert palindrome('not a palindrome') is False
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_fifth():
        """
        Palindrome('a') should return true.
        """
        assert palindrome('a') is True
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_sixth():
        """
        Palindrome('test') should return false.
        """
        assert palindrome('test') is False
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_seventh():
        """
        Palindrome('sedes') should return true.
        """
        assert palindrome('sedes') is True
    
    
    @pytest.mark.palindrome_test_case
    def test_palindrome_eighth():
        """
        Palindrome('almostomla') should return false.
        """
        assert palindrome('almostomla') is False
                ''',
            ),
        )
        TasksStatistics.objects.create(
            task_title=Tasks.objects.get(task_title="Palindrome Checker"),
            sum_of_all_tries_per_task=0,
            sum_of_all_successful_submission_per_task=0,
        )


def create_blank_user_solution_file() -> None:
    """
    This method was created because functional tests running locally throws errors is use_solution
    file doesn't exists.
    """
    expected_file_loc = path.join(
        path.dirname(path.realpath(__file__)),
        "remote_code_execution_app",
        "tests",
        "user_solution.py",
    )

    with open(expected_file_loc, "a"):
        pass


if __name__ == "__main__":
    create_super_user()
    create_tasks()
