from django.urls import path
from django.contrib.auth.decorators import login_required

# Own
from . import views

urlpatterns = [
    path("<int:pk>/", login_required(views.CodeEditorView.as_view()), name="editor-view"),
    path("compile/", views.send_converted_tests_cases_output, name="run-code"),
]
