from django.urls import path

# Own
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("main-page/", views.MainPageView.as_view(), name="main-page"),
    path("tasks/", views.render_tasks_data, name="send-converted-tasks-data"),
]
