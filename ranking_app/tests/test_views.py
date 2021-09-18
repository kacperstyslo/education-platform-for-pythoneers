from django.urls import resolve, reverse
from django.test import Client, TestCase


class TestRankingView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.starting_page_url = reverse("ranking-page")
        self.response = self.client.get(self.starting_page_url)

    def test_if_ranking_view_render_on_indicated_url(self) -> None:
        found = resolve("/ranking/")
        self.assertEqual(
            found.view_name,
            "ranking-page",
            msg="View name on route '/ranking/' should be 'ranking-page'",
        )

    def test_name_of_rendered_template_to_ranking_view(self) -> None:
        """
        View RankingPage should render rankingtable_list.html template.
        """
        self.assertTemplateUsed(self.response, "ranking_app/rankingtable_list.html")

    def test_anonymous_user_get_on_ranking_page(self) -> None:
        self.assertEqual(
            self.response.status_code,
            200,
            msg="If anonymous user try to see code ranking page, server should return 200",
        )
