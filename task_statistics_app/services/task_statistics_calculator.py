# Own
from users_app.models import UsersTasksSolutions
from task_statistics_app.db.models_operators import SuccessfulSubmission


def calc_task_success_rate(task_title: str) -> str:
    """
    Caller: remote_code_execution_app.views.CodeEditorView

    This method calculate task success rate for chosen task and represent result in % format.
    """
    num_of_users_try_to_complete_task: int = UsersTasksSolutions.objects.filter(
        task_title=task_title
    ).count()
    successful_submission: int = SuccessfulSubmission(task_title).get_all()
    try:
        success_rate: float = successful_submission / num_of_users_try_to_complete_task
    except ZeroDivisionError:
        success_rate = 0.0
    return "{0:.0%}".format(success_rate)
