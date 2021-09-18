from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Own
from users_app.forms import UserRegistrationForm


class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("user-login")
    template_name = "users_app/registration_page.html"
