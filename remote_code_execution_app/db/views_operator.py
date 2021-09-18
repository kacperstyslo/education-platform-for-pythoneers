from typing import Union

# Own
from users_app.models import UsersTasksSolutions


def get_saved_user_solution_from_db(user_id: int, task_title: str) -> Union[str, None]:
    """
    Caller: remote_code_execution_app.services.

    This method check if user solution to task exist in 'User Task Solutions' table, if it is,
    method will return it.
    """
    if UsersTasksSolutions.objects.filter(task_title=task_title, user_nickname=user_id).exists():
        return UsersTasksSolutions.objects.values_list("user_solution", flat=True).get(
            task_title=task_title, user_nickname=user_id
        )
    return None
