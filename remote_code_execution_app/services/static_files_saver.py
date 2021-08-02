from pathlib import Path

TESTS_DIR = Path(__file__).parent.parent / "tests"


def save_locally(file_name: str, content: str) -> None:
    """
    Caller: remote_code_execution_app.views.CodeEditorView &
            remote_code_execution_app.views.send_converted_tests_cases_output

    This method saves data locally on the server. Used by the
    remote_code_execution_app.views.CodeEditorView to save tests (downloaded from the
    database) to tasks and the code written by the user.
    """
    with open(TESTS_DIR / file_name, mode="w") as file:
        file.write(content)
