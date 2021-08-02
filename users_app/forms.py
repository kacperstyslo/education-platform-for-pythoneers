from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """
    Custom user form based on built in django 'UserCreationForm' form.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name in ["email", "username", "password1", "password2"]:
            self.fields[field_name].help_text = None

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "password1",
            "password2",
        )
        labels = {"username": "Login"}
