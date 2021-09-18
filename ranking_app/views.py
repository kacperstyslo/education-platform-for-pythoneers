from django.views.generic.list import ListView

# Own
from ranking_app.models import RankingTable

# Own
# My services
from ranking_app.services.points_calculator import UsersPointsCalculator


class RankingView(ListView):
    """
    This class based view rendering ranking page view.
    """

    model = RankingTable
    context_object_name = "ranking_table"

    def get_context_data(self, **kwargs):
        UsersPointsCalculator()()
        return super().get_context_data(**kwargs)
