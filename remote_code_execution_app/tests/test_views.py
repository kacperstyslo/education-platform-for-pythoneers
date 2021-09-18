from django.urls import reverse
from django.test import Client, TestCase


class TestCodeEditorView(TestCase):
    def test_anonymous_user_get_on_code_editor_page(self) -> None:
        client = Client()
        starting_page_url = reverse("editor-view", kwargs={"pk": 1})
        response = client.get(starting_page_url)
        self.assertEqual(
            response.status_code,
            302,
            msg="If anonymous user try to see code editor page, server should return 302",
        )
