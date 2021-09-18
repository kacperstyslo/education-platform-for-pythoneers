from django.conf import settings
from django.test import TestCase


class MainSettingsTest(TestCase):
    def setUp(self) -> None:
        self.installed_apps = settings.INSTALLED_APPS

    def test_if_are_created_apps_added_to_main_settings_file(self) -> None:
        """
        These tests were created to make sure that all created applications are in the application's
        main settings file.
        """
        self.assertIn("main_app", self.installed_apps, msg="Should return True")
        self.assertIn("remote_code_execution_app", self.installed_apps, msg="Should return True")
        self.assertIn("users_app", self.installed_apps, msg="Should return True")
        self.assertIn("ranking_app", self.installed_apps, msg="Should return True")
        self.assertIn("task_statistics_app", self.installed_apps, msg="Should return True")
        self.assertIn("crispy_forms", self.installed_apps, msg="Should return True")
        self.assertIn("storages", self.installed_apps, msg="Should return True")
