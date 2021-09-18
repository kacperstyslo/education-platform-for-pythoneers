from django.urls import path
from django.contrib.auth import views as auth_views

# Own
from . import views

urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="user-registration"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True, template_name="registration/login.html"
        ),
        name="user-login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="main-page"), name="logout"),
]
