# pylint: disable=C0411,C0412

from typing import Any, Dict

from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse, QueryDict

# Own
from main_app.models import Tasks
# Own
# DB operators
from remote_code_execution_app.db.views_operator import get_saved_user_solution_from_db
from task_statistics_app.db.models_operators import SuccessfulSubmission
# Own
# My services
from task_statistics_app.services.task_statistics_calculator import calc_task_success_rate
from remote_code_execution_app.services import (
    solution_tester,
    static_files_saver,
    token_generator,
    tests_cases_counter,
)


class CodeEditorView(DetailView):
    """
    This class based view generating code editor view.
    """

    model = Tasks
    context_object_name = "chosen"
    template_name = "remote_code_execution_app/code_editor.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        task_title: str = Tasks.objects.get(task_id=self.kwargs["pk"])

        static_files_saver.save_locally(
            file_name="test_user_solution.py",
            content=list(Tasks.objects.filter(task_title=task_title).values("task_tests"))[0].get(
                "task_tests"
            ),
        )

        context["task_token"] = token_generator.generate_token()
        context["user_code"] = get_saved_user_solution_from_db(
            user_id=self.request.user, task_title=task_title
        )
        context["successful_submission_per_task"] = SuccessfulSubmission(task_title).get_all()
        context["success_rate_per_task"] = calc_task_success_rate(task_title)

        return context


def send_converted_tests_cases_output(request: QueryDict) -> HttpResponse:
    """
    This method send data to method that responsible for saving user code locally. this method
    also send user code to service ('solution_tester') what is responsible for testing user code.
    After receiving the converted data from the testing services ('solution_tester'), this method
    will send converted tests cases output to the user.
    """
    static_files_saver.save_locally(file_name="user_solution.py", content=str(request.GET["code"]))

    test_case_output = solution_tester.LocalUserSolutionTester(
        task_id=int(request.GET["task"]),
        task_title=Tasks.objects.only("task_title").get(task_id=int(request.GET["task"])),
        user_id=request.user.id,
        user_code=request.GET["code"],
        number_of_tests_cases=tests_cases_counter.count_num_of_tests_cases_in_task(),
    )()
    return JsonResponse(data=test_case_output)
