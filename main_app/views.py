from typing import Union

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

# Own
# DB operator
from main_app.db.views_operator import get_tasks_data_from_db


class StartingPageView(TemplateView):
    """
    This view only generating starting page.
    """

    template_name = "main_app/starting_page.html"


class MainPageView(TemplateView):
    """
    This view only generating main page.
    """

    template_name = "main_app/main_page.html"


@login_required
def render_tasks_data(
    request: HttpRequest,
) -> Union[HttpResponse, HttpResponseRedirect]:
    """
    This method render already converted data.
    """
    return JsonResponse(get_tasks_data_from_db(), safe=False)
