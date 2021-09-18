import ast

# Own
from remote_code_execution_app.services.static_files_saver import TESTS_DIR


def count_num_of_tests_cases_in_task() -> int:
    """
    Caller: remote_code_execution_app.views.send_converted_tests_cases_output

    This method counts the number of tests case in the test file.
    """
    with open(TESTS_DIR / "test_user_solution.py", "r") as file:
        tree = ast.parse(file.read())
        number_of_tests = sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)
    return number_of_tests
