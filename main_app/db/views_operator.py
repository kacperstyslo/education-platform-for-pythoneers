from typing import Dict, List, Union

# Own
from main_app.models import Tasks


def get_tasks_data_from_db() -> List[Dict[str, Union[str, bool]]]:
    """
    Caller: main_app.views.render_tasks_data

    This method retrieves data about tasks from the table 'Tasks'. Converts the data to a list
    type (because it is easier to manage the data) and send converted data to MainPageView view.
    """
    return list(Tasks.objects.all().values())
