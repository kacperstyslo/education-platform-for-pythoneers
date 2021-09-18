from django.urls import resolve, reverse
from django.test import Client, TestCase


class TestStartingPageView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.starting_page_url = reverse("starting-page")
        self.response = self.client.get(self.starting_page_url)

    def test_if_starting_page_view_render_on_indicated_url(self) -> None:
        found = resolve("/")
        self.assertEqual(
            found.view_name, "starting-page", msg="View name on route '/' should be starting-page"
        )

    def test_name_of_rendered_template_to_starting_page_view(self) -> None:
        """
        View StartingPage should render starting_page.html template.
        """
        self.assertTemplateUsed(self.response, "main_app/starting_page.html")

    def test_anonymous_user_get_on_starting_page(self) -> None:
        self.assertEqual(
            self.response.status_code,
            200,
            msg="If anonymous user try to see code starting page, server should return 200",
        )


class MainPageViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.starting_page_url = reverse("main-page")
        self.response = self.client.get(self.starting_page_url)

    def test_if_main_page_view_render_on_indicated_url(self) -> None:
        found = resolve("/main-page/")
        self.assertEqual(
            found.view_name, "main-page", msg="View name on route '/main-page/' should be main-page"
        )

    def test_if_send_converted_task_data_render_on_indicated_url(self) -> None:
        found = resolve("/tasks/")
        self.assertEqual(
            found.view_name,
            "send-converted-tasks-data",
            msg="View name on route '/tasks/' should be 'send-converted-tasks-data'",
        )

    def test_name_of_rendered_template_to_main_page_view(self) -> None:
        """
        View MainPage should render main_page.html template.
        """
        self.assertTemplateUsed(self.response, "main_app/main_page.html")

    def test_anonymous_user_get_on_main_page(self) -> None:
        self.assertEqual(
            self.response.status_code,
            200,
            msg="If anonymous user try to see code main page, server should return 200",
        )
