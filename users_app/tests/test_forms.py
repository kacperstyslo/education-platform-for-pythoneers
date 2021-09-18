from django.test import TestCase

# Own
from users_app.forms import UserRegistrationForm


class TestUserRegistrationForm(TestCase):
    def test_user_registration_form_no_data(self) -> None:
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid(), msg="Should be False")

    def test_user_registration_form_if_email_is_blank(self) -> None:
        form = UserRegistrationForm(
            data={
                "email": "",
                "username": "test_user12345",
                "password1": "secret_password",
                "password2": "secret_password",
            }
        )
        self.assertTrue(form.is_valid(), msg="Should be True")

    def test_user_registration_form_if_username_is_blank(self) -> None:
        form = UserRegistrationForm(
            data={
                "email": "test@test.com",
                "username": "",
                "password1": "secret_password",
                "password2": "secret_password",
            }
        )
        self.assertFalse(form.is_valid(), msg="Should be False")

    def test_user_registration_form_if_password1_is_blank(self) -> None:
        form = UserRegistrationForm(
            data={
                "email": "test@test.com",
                "username": "test_user12345",
                "password1": "",
                "password2": "secret_password",
            }
        )
        self.assertFalse(form.is_valid(), msg="Should be False")

    def test_user_registration_form_if_password2_is_blank(self) -> None:
        form = UserRegistrationForm(
            data={
                "email": "test@test.com",
                "username": "test_user12345",
                "password1": "secret_password",
                "password2": "",
            }
        )
        self.assertFalse(form.is_valid(), msg="Should be False")

    def test_user_registration_form_if_password1_and_password2_is_blank(self) -> None:
        form = UserRegistrationForm(
            data={
                "email": "test@test.com",
                "username": "test_user12345",
                "password1": "",
                "password2": "",
            }
        )
        self.assertFalse(form.is_valid(), msg="Should be False")

    def test_user_registration_form_if_all_required_data_is_provided_correctly(self) -> None:
        form = UserRegistrationForm(
            data={
                "email": "test@test.com",
                "username": "test_user12345",
                "password1": "secret_password",
                "password2": "secret_password",
            }
        )
        self.assertTrue(form.is_valid(), msg="Should be True")
