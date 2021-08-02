from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("main_app.urls")),
    path("admin/", admin.site.urls),
    path("tasks/", include("remote_code_execution_app.urls")),
    path("accounts/", include("users_app.urls")),
    path("ranking/", include("ranking_app.urls")),
]
